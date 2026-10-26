"""Render a PO file's translation changes as inline red/green diffs on the built HTML page.

Builds the page twice (base version of the PO, then the working-tree version), finds every
entry whose msgstr changed, injects an inline diff into the new page's paragraph, and saves
one screenshot per changed paragraph plus a stitched overview.

usage (from the repo root):
  uv run --no-project --with polib --with beautifulsoup4 --with playwright --with pillow \
    python .claude/skills/review-rendered-diff/scripts/render_diff.py howto/logging.po --base origin/3.15

Outputs go to .render-review/<po path without .po>/ unless --out is given.
"""
import argparse
import copy
import difflib
import re
import subprocess
import sys
from pathlib import Path

import polib
from bs4 import BeautifulSoup, NavigableString
from PIL import Image
from playwright.sync_api import Error as PlaywrightError
from playwright.sync_api import sync_playwright

BLOCKS = ["p", "h1", "h2", "h3", "h4", "h5", "li", "dt", "dd", "th", "td", "caption"]
# characters that reST turns into markup, so they never appear verbatim in the rendered text
MARKUP = re.compile(r"[`*\\|_<>]|:[a-z:]+:")
CSS = """
del.rr-del{background:#ffd7d5;color:#82071e;text-decoration:line-through;text-decoration-thickness:1.5px;border-radius:3px;padding:0 1px}
ins.rr-ins{background:#aceebb;color:#055d20;text-decoration:none;border-radius:3px;padding:0 1px}
.rr-target{outline:2px dashed #d4a72c;outline-offset:6px;border-radius:2px}
.rr-pair{margin:1em 0;outline:2px dashed #d4a72c;outline-offset:6px;border-radius:2px}
.rr-side{border-left:4px solid;padding:2px 12px;margin:6px 0;border-radius:4px}
.rr-side>*:not(.rr-tag){margin:.35em 0}
.rr-side.rr-old{background:#f6f8fa;border-color:#8c959f}
.rr-side.rr-old.rr-rewrite{background:#ffebe9;border-color:#cf222e}
.rr-side.rr-new{background:#e6ffec;border-color:#1a7f37}
.rr-tag{display:inline-block;font:600 11px/1 -apple-system,"Segoe UI",sans-serif;color:#fff;padding:3px 6px;border-radius:4px;margin-top:6px}
.rr-old .rr-tag{background:#57606a}.rr-old.rr-rewrite .rr-tag{background:#cf222e}.rr-new .rr-tag{background:#1a7f37}
.rr-pair a.headerlink{display:none}
"""
# block elements that must keep their place in a table/list: the pair goes inside them
CELLS = {"li", "dt", "dd", "th", "td"}
CJK = re.compile(r"[㐀-鿿豈-﫿]")


def cjk_share(text):
    # URLs are untranslated by nature; a short Chinese sentence around a long URL is still Chinese
    letters = [c for c in re.sub(r"[a-z]+://[\x21-\x7e]+", "", text) if c.isalpha()]
    return sum(bool(CJK.match(c)) for c in letters) / len(letters) if letters else 0.0


def choose_mode(args, base_msgstr, old_txt, new_txt):
    """inline red/green, or two blocks when a char diff would be all red/green noise."""
    if args.mode != "auto":
        return args.mode, ""
    if not base_msgstr or (cjk_share(old_txt) < 0.2 <= cjk_share(new_txt)):
        return "blocks", "new translation"
    # SequenceMatcher.ratio() overrates CJK rewrites (common characters keep matching), so
    # measure the share of characters that changed instead
    ops = difflib.SequenceMatcher(None, old_txt, new_txt, autojunk=False).get_opcodes()
    changed = sum(max(i2 - i1, j2 - j1) for op, i1, i2, j1, j2 in ops if op != "equal")
    share = changed / max(len(new_txt), 1)
    # short text (headings, table cells) reads fine inline even when most characters change
    if len(new_txt.strip()) >= 30 and share > args.rewrite_threshold:
        return "blocks", f"rewritten, {share:.0%} changed"
    return "inline", ""


def strip_ids(el):
    for tagged in [el, *el.find_all(id=True)]:
        tagged.attrs.pop("id", None)
    return el


def make_pair(soup, old_el, new_el, n, translation):
    """Replace new_el (in place in the page) with stacked old/new blocks."""
    pair = soup.new_tag("div", attrs={"class": "rr-pair", "data-rr": str(n)})
    old_cls = "rr-side rr-old" + ("" if translation else " rr-rewrite")
    labels = ("原文 (English)", "譯文") if translation else ("修改前", "修改後")
    for cls, el, label in ((old_cls, old_el, labels[0]), ("rr-side rr-new", new_el, labels[1])):
        side = soup.new_tag("div", attrs={"class": cls})
        tag = soup.new_tag("span", attrs={"class": "rr-tag"})
        tag.string = label
        side.append(tag)
        if el.name in CELLS:  # keep only the cell/item contents, the pair sits inside the cell
            body = soup.new_tag("div")
            for child in list(copy.copy(el).contents):
                body.append(child)
            side.append(strip_ids(body))
        else:
            side.append(strip_ids(copy.copy(el)))
        pair.append(side)
    if new_el.name in CELLS:
        new_el.clear()
        new_el.append(pair)
    else:
        new_el.replace_with(pair)


def sh(cmd, **kw):
    return subprocess.run(cmd, check=True, text=True, capture_output=True, **kw).stdout


def build_page(cpython_doc, sphinx, po_rel, po_text, work):
    """Build one page in isolation; return the HTML path or None.

    The PO text goes into a private locale dir and Sphinx writes to `work`, so neither the
    repo working tree nor ../cpython/Doc/locales is touched (unlike `make build`, which
    hard-links the PO into cpython). Sphinx usually exits 1 because of unrelated CPython
    redirect warnings, so success is judged by the HTML file existing, not the exit code.
    """
    loc = work / "locales" / "zh_TW" / "LC_MESSAGES" / po_rel
    loc.parent.mkdir(parents=True, exist_ok=True)
    loc.write_text(po_text, encoding="utf-8")
    rst = cpython_doc / Path(po_rel).with_suffix(".rst")
    html = work / "html" / Path(po_rel).with_suffix(".html")
    with open(work / "build.log", "w") as log:
        subprocess.run([sphinx, "-q", "-b", "html", "-j", "auto", "-D", "language=zh_TW",
                        "-D", f"locale_dirs={work / 'locales'}", "-D", "gettext_compact=0",
                        "-d", str(work / "doctrees"), str(cpython_doc), str(work / "html"), str(rst)],
                       check=False, stdout=log, stderr=subprocess.STDOUT)
    return html if html.exists() else None


def snippet(msgstr):
    """Longest run of plain text (no reST markup) — it survives rendering verbatim."""
    text = msgstr.replace("\n", " ").rstrip()
    # literal-block marker: "文字： ::" renders as "文字：", "text::" renders as "text:"
    text = re.sub(r"\s+::$", "", text)
    text = re.sub(r"::$", ":", text)
    # roles, inline literals and links render differently from their source (`~Handler.setFormatter`
    # becomes "setFormatter()"), so drop them entirely instead of keeping their contents
    text = re.sub(r"(?::[\w:.+-]+:)?`[^`]*`_{0,2}|``[^`]*``", "\0", text)
    runs = [r.strip() for r in MARKUP.split(text.replace("\0", "|"))]
    return max(runs, key=len) if runs else ""


def plain(msgstr):
    """Rough rendered text of an entry, used only to pick between several matching blocks."""
    text = " ".join(msgstr.split())
    text = re.sub(r"::$", ":", re.sub(r"\s+::$", "", text))
    text = re.sub(r"``([^`]*)``", r"\1", text)
    text = re.sub(r"(?::[\w:.+-]+:)?`([^`<]*?)\s*(?:<[^>]*>)?`_{0,2}", lambda m: m[1].lstrip("!~"), text)
    return re.sub(r"\\ ?|\*", "", text)


def highlighted(el):
    return "rr-target" in el.get("class", []) or el.find_parent(class_="rr-pair") is not None


def find_block(soup, text, full=""):
    """Smallest block containing the snippet. When the snippet is not unique (two sentences that
    share a phrase), prefer blocks not yet highlighted, then the one closest to the full text."""
    body = soup.select_one("div[role=main]") or soup.select_one("div.body") or soup.body
    # rendered text keeps the source's line breaks and double spaces; msgid snippets don't
    text = " ".join(text.split())
    hits = [el for el in body.find_all(BLOCKS) if text and text in " ".join(el.get_text().split())]
    if len(hits) < 2:
        return hits[0] if hits else None

    def rank(el):
        el_txt = " ".join(el.get_text().split())
        similarity = difflib.SequenceMatcher(None, full, el_txt, autojunk=False).ratio() if full else 0
        return (highlighted(el), -similarity, len(el_txt))
    return min(hits, key=rank)


def visible(text):
    """A changed run that is only whitespace would render as an empty colored box."""
    return "␣" * len(text) if text.isspace() else text


def inline_diff(soup, el, old_txt):
    """Rewrite el in place: inserted text -> <ins>, deleted old text -> <del> at the same spot."""
    new_txt = el.get_text()
    ops = difflib.SequenceMatcher(None, old_txt, new_txt, autojunk=False).get_opcodes()
    ins = [(j1, j2) for op, _, _, j1, j2 in ops if op in ("replace", "insert")]
    dels = [(j1, old_txt[i1:i2]) for op, i1, i2, j1, _ in ops if op in ("replace", "delete")]
    total, pos = len(new_txt), 0
    for node in list(el.descendants):
        if not isinstance(node, NavigableString) or node.parent.name in ("script", "style"):
            continue
        text = str(node)
        start, end = pos, pos + len(text)
        pos = end
        points = [(p - start, t) for p, t in dels if start <= p < end or p == end == total]
        spans = [(max(a, start) - start, min(b, end) - start) for a, b in ins if a < end and b > start]
        if not points and not spans:
            continue
        cuts = sorted({0, len(text), *(p for p, _ in points), *(c for s in spans for c in s)})
        pieces = []
        for k, c in enumerate(cuts):
            for p, t in points:
                if p == c:
                    tag = soup.new_tag("del", attrs={"class": "rr-del"})
                    tag.string = visible(t)
                    pieces.append(tag)
            if k + 1 < len(cuts):
                seg = text[c:cuts[k + 1]]
                if any(a <= c and cuts[k + 1] <= b for a, b in spans):
                    tag = soup.new_tag("ins", attrs={"class": "rr-ins"})
                    tag.string = visible(seg)
                    pieces.append(tag)
                else:
                    pieces.append(NavigableString(seg))
        for p in pieces:
            node.insert_before(p)
        node.extract()


def changed_entries(base_po, new_po):
    # Sphinx skips fuzzy entries, so on the rendered page a fuzzy msgstr is the same as none
    def rendered(e):
        return "" if "fuzzy" in e.flags else e.msgstr
    base = {(e.msgctxt, e.msgid): rendered(e) for e in base_po}
    return [e for e in new_po if rendered(e) and base.get((e.msgctxt, e.msgid), "") != e.msgstr
            and e.msgid != e.msgstr], base


def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("po", nargs="+", help="PO path(s) relative to repo root, e.g. howto/logging.po")
    ap.add_argument("--base", default="origin/3.15", help="git ref holding the 'before' version")
    ap.add_argument("--new", help="git ref for the 'after' version (default: working-tree file)")
    ap.add_argument("--out", help="output dir (default .render-review/<po without .po>)")
    ap.add_argument("--context", type=int, default=140, help="px of page kept above/below")
    ap.add_argument("--mode", choices=["auto", "inline", "blocks"], default="auto",
                    help="auto: two blocks for new translations / rewrites, inline diff otherwise")
    ap.add_argument("--rewrite-threshold", type=float, default=0.5,
                    help="auto mode: above this share of changed characters (text >= 30 chars), "
                         "show two blocks instead of inline")
    ap.add_argument("--cpython", default="../cpython", help="CPython clone (Makefile CPYTHON_CLONE)")
    ap.add_argument("--sphinx", default=str(Path("~/.venvs/python-docs-i18n/bin/sphinx-build").expanduser()))
    return ap.parse_args()


def main(args, po_rel, repo, cpython_doc):
    """Render one PO file. Returns False if it could not be rendered."""
    print(f"== {po_rel}")
    sub = Path(po_rel).with_suffix("")
    if args.out:
        base_out = Path(args.out).resolve()
        out = base_out / sub if len(args.po) > 1 else base_out
    else:
        out = repo / ".render-review" / sub
    out.mkdir(parents=True, exist_ok=True)

    base_text = sh(["git", "show", f"{args.base}:{po_rel}"], cwd=repo)
    new_text = (sh(["git", "show", f"{args.new}:{po_rel}"], cwd=repo) if args.new
                else (repo / po_rel).read_text(encoding="utf-8"))
    entries, base_map = changed_entries(polib.pofile(base_text), polib.pofile(new_text))
    if not entries:
        print(f"no msgstr changes in {po_rel} versus {args.base}")
        return True
    print(f"{len(entries)} changed entries; building both versions (~20s each)")

    old_html = build_page(cpython_doc, args.sphinx, po_rel, base_text, out / "build-old")
    new_html = build_page(cpython_doc, args.sphinx, po_rel, new_text, out / "build-new")
    for name, html in (("old", old_html), ("new", new_html)):
        if html is None:
            print(f"{name} build produced no HTML; see {out / f'build-{name}' / 'build.log'}")
            return False
    page = new_html  # the diff page is written next to it so ../_static assets resolve
    for stale in out.glob("diff-*.png"):
        stale.unlink()

    old = BeautifulSoup(old_html.read_text(encoding="utf-8"), "html.parser")
    new = BeautifulSoup(new_html.read_text(encoding="utf-8"), "html.parser")
    style = new.new_tag("style")
    style.string = CSS
    new.head.append(style)

    report, done = [], 0
    for e in entries:
        base_msgstr = base_map.get((e.msgctxt, e.msgid), "")
        new_el = find_block(new, snippet(e.msgstr), plain(e.msgstr))
        # a newly translated entry shows the English msgid on the old page
        old_el = find_block(old, snippet(base_msgstr or e.msgid), plain(base_msgstr or e.msgid))
        label = f"L{e.linenum}"
        if new_el is None or old_el is None:
            report.append(f"{label}: SKIPPED (paragraph not found in rendered page) — {e.msgid[:60]!r}")
            continue
        if highlighted(new_el):
            report.append(f"{label}: same paragraph as an earlier entry, already highlighted")
            continue
        done += 1
        mode, why = choose_mode(args, base_msgstr, old_el.get_text(), new_el.get_text())
        if mode == "blocks":
            english_before = not base_msgstr or cjk_share(old_el.get_text()) < 0.2
            make_pair(new, old_el, new_el, done, translation=english_before)
        else:
            inline_diff(new, new_el, old_el.get_text())
            new_el["class"] = [*new_el.get("class", []), "rr-target"]
            new_el["data-rr"] = str(done)
        report.append(f"{label}: diff-{done}.png [{mode}{': ' + why if why else ''}] — {e.msgid[:60]!r}")

    # write next to the real page so ../_static assets resolve
    diff_page = page.with_name(page.stem + "-diff.html")
    diff_page.write_text(str(new), encoding="utf-8")

    rect = """s => { const r = document.querySelector(s).getBoundingClientRect();
                     return {x: r.left + scrollX, y: r.top + scrollY, w: r.width, h: r.height}; }"""
    shots = []
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(channel="chrome")
        except PlaywrightError:  # no local Chrome; use bundled Chromium
            browser = p.chromium.launch()
        pg = browser.new_page(viewport={"width": 1100, "height": 900}, color_scheme="light",
                              device_scale_factor=2)
        pg.goto(diff_page.as_uri())
        pg.wait_for_load_state("networkidle")
        height = pg.evaluate("document.documentElement.scrollHeight")
        col = pg.evaluate(rect, "div.body")
        for n in range(1, done + 1):
            b = pg.evaluate(rect, f"[data-rr='{n}']")
            top, bottom = max(0, b["y"] - args.context), min(height, b["y"] + b["h"] + args.context)
            path = out / f"diff-{n}.png"
            pg.screenshot(path=str(path), full_page=True,
                          clip={"x": col["x"] - 20, "y": top, "width": col["w"] + 40, "height": bottom - top})
            shots.append(path)
        browser.close()

    if shots:
        ims = [Image.open(s).convert("RGB") for s in shots]
        gap = 28
        sheet = Image.new("RGB", (max(i.width for i in ims), sum(i.height for i in ims) + gap * (len(ims) + 1)), "#d0d7de")
        y = gap
        for im in ims:
            sheet.paste(im, (0, y))
            y += im.height + gap
        sheet.save(out / "all-diffs.png")

    print("\n".join(report))
    print(f"diff page : {diff_page}")
    print(f"screens   : {out}/diff-*.png, overview {out/'all-diffs.png'}")
    return True


if __name__ == "__main__":
    args = parse_args()
    repo = Path(sh(["git", "rev-parse", "--show-toplevel"]).strip())
    cpython_doc = (repo / args.cpython / "Doc").resolve()
    if not (cpython_doc / "conf.py").exists():
        sys.exit(f"no CPython Doc at {cpython_doc}; run `make prepare_deps` once")
    results = [main(args, po, repo, cpython_doc) for po in args.po]
    sys.exit(0 if all(results) else 1)
