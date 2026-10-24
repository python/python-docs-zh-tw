"""Build translated pages and check the rendered HTML text.

Usage (from the repo root)::

    python3 .scripts/render_review.py library/dataclasses.po [faq/library.po ...]
        [--cpython ../cpython] [--no-build] [--out DIR]

For each PO file this script:

1. hard-links it into the CPython clone's ``Doc/locales`` and builds only the
   matching page with Sphinx (same options as ``make build``);
2. extracts the rendered prose of the page (code blocks removed) into
   ``<out>/<page>.txt`` so it can be read as a reader would see it;
3. reports heuristic findings with the paragraph they occur in.

Findings are hints, not errors: read the text file and confirm each one.
Only the standard library is needed; the build needs the docs venv from
``make prepare_deps`` (``~/.venvs/python-docs-i18n``).
"""

import argparse
import os
import re
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
VENV = Path.home() / ".venvs" / "python-docs-i18n"
CJK = "㐀-䶿一-鿿"

# Labels produced by Sphinx's own zh_TW catalog, not by this repo.
SPHINX_LABELS = re.compile(r"在 \d+\.\d+ 版(被加入|的變更|之後被棄用|中被移除)[.:]")

ZH_CN = ["函數", "返回", "對象", "默認", "字符串", "調用", "信息", "支持",
         "創建", "代碼", "迭代", "生成", "設置", "實現", "鏈接", "聲明",
         "運行", "數據", "線程", "進程", "內存", "異常", "模塊", "緩存"]

CHECKS = [
    ("leftover reST role", re.compile(
        r":(meth|func|class|attr|term|ref|exc|const|data|mod|deco|pep|"
        r"program|keyword|envvar|option|file|samp|source):`?")),
    ("raw reST markup", re.compile(r"``|`_|\*\*[^\s*,)][^*]*\*\*")),
    ("literal backslash", re.compile(r"\\ ")),
    ("no space between CJK and Latin/digit", re.compile(
        rf"[{CJK}][A-Za-z0-9_]|[A-Za-z0-9_][{CJK}]")),
    ("half-width punctuation after CJK", re.compile(rf"[{CJK}][,;:!?()]")),
    ("space before full-width punctuation", re.compile(r" [，。、：；！？）」]")),
    ("space after full-width bracket/punctuation", re.compile(
        rf"[（「，。、：；）」] [{CJK}]")),
    ("space between CJK characters", re.compile(rf"[{CJK}] [{CJK}]")),
    ("zh_CN wording", re.compile("|".join(ZH_CN))),
]


class BodyText(HTMLParser):
    """Collect block-level text inside ``div.body``, skipping code blocks."""

    BLOCKS = {"p", "li", "dt", "h1", "h2", "h3", "h4", "th", "td", "caption"}
    SKIP = {"pre", "script", "style"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.depth = 0          # >0 while inside div.body
        self.skip = 0           # >0 while inside skipped elements
        self.stack = []
        self.blocks = []        # (tag, text)
        self.cur = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = a.get("class", "") or ""
        if self.depth == 0:
            if tag == "div" and "body" in cls.split():
                self.depth = 1
                self.stack = ["div"]
            return
        self.stack.append(tag)
        if tag in self.SKIP or "headerlink" in cls or "highlight" in cls:
            self.skip += 1
            self.stack[-1] = ("skip", tag)
            return
        if tag in self.BLOCKS and self.skip == 0:
            self._flush()
            self.cur = [tag, ""]

    def handle_endtag(self, tag):
        if self.depth == 0 or not self.stack:
            return
        top = self.stack.pop()
        if isinstance(top, tuple):
            self.skip -= 1
        if tag in self.BLOCKS:
            self._flush()
        if not self.stack:
            self._flush()
            self.depth = 0

    def handle_data(self, data):
        if self.depth and not self.skip and self.cur is not None:
            self.cur[1] += data

    def _flush(self):
        if self.cur:
            text = " ".join(self.cur[1].split())
            if text and text != "¶":
                self.blocks.append((self.cur[0], text.rstrip("¶").strip()))
        self.cur = None


def build(pos, cpython):
    lc = cpython / "Doc" / "locales" / "zh_TW" / "LC_MESSAGES"
    for po in pos:
        dst = lc / po
        dst.parent.mkdir(parents=True, exist_ok=True)
        if dst.exists():
            dst.unlink()
        os.link(REPO / po, dst)  # re-link: editors and sed replace the inode
    sources = " ".join(str(Path(p).with_suffix(".rst")) for p in pos)
    env = dict(os.environ, PATH=f"{VENV / 'bin'}:{os.environ['PATH']}")
    cmd = ["make", "-C", str(cpython / "Doc"), "html", f"SOURCES={sources}",
           "SPHINXOPTS=-j auto -D language=zh_TW -D locale_dirs=locales "
           "-D gettext_compact=0"]
    res = subprocess.run(cmd, env=env, capture_output=True, text=True)
    if res.returncode:
        # The docs Makefile treats warnings as errors; unrelated redirect
        # warnings are common in a reused build dir, so only warn here.
        warn = [l for l in res.stdout.splitlines() + res.stderr.splitlines()
                if "WARNING" in l or "ERROR" in l]
        print("build reported problems (pages may still be fine):",
              *warn[:10], sep="\n  ", file=sys.stderr)


def review(po, cpython, out):
    html = cpython / "Doc" / "build" / "html" / Path(po).with_suffix(".html")
    if not html.exists():
        print(f"{po}: {html} not found (build failed?)")
        return 1
    parser = BodyText()
    parser.feed(html.read_text(encoding="utf-8"))
    txt = out / Path(po).with_suffix(".txt")
    txt.parent.mkdir(parents=True, exist_ok=True)
    lines = []
    for n, (tag, text) in enumerate(parser.blocks, 1):
        lines.append(("## " if tag.startswith("h") else "- ") + text)
    txt.write_text("\n".join(lines) + "\n", encoding="utf-8")

    findings = 0
    english = 0
    print(f"\n=== {po}\n    rendered text: {txt}")
    for n, line in enumerate(lines, 1):
        text = SPHINX_LABELS.sub("", line)
        for name, rx in CHECKS:
            for m in rx.finditer(text):
                s = max(0, m.start() - 15)
                print(f"  L{n} [{name}] …{text[s:m.end() + 15]}…")
                findings += 1
        letters = re.findall(rf"[A-Za-z{CJK}]", text)
        cjk = re.findall(rf"[{CJK}]", text)
        if len(letters) > 40 and len(cjk) / len(letters) < 0.05:
            english += 1
    print(f"  {findings} findings; {english} paragraphs still in English "
          "(untranslated, or msgid older than the CPython clone)")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("po", nargs="+", help="PO files relative to the repo root")
    ap.add_argument("--cpython", default=str(REPO.parent / "cpython"))
    ap.add_argument("--no-build", action="store_true")
    ap.add_argument("--out", default=str(REPO / ".render-review"))
    args = ap.parse_args()
    cpython = Path(args.cpython).resolve()
    if not (cpython / "Doc" / "conf.py").exists():
        sys.exit(f"CPython clone not found at {cpython} (run make prepare_cpython)")
    if not args.no_build:
        build(args.po, cpython)
    out = Path(args.out)
    return max(review(po, cpython, out) for po in args.po)


if __name__ == "__main__":
    sys.exit(main())
