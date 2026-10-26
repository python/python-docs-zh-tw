---
name: review-rendered-diff
description: Use when a reviewer needs to see how changed PO translations look on the rendered Python docs page — before/after comparison, red/green inline diff on the built HTML, or screenshots of changed paragraphs for a PR description or review comment.
argument-hint: <po-file> [--base <git-ref>] [--new <git-ref>]
---

# review-rendered-diff

Show translation changes **inside the real rendered page**, each changed paragraph outlined,
one screenshot per paragraph plus an overview image. Each entry is shown one of three ways:

| Change | Shown as | Picked when (`--mode auto`) |
|---|---|---|
| Edit of an existing translation | **inline**: deleted text red with strikethrough, inserted green | default |
| English → Chinese (new translation) | **two blocks**: gray「原文 (English)」above green「譯文」 | base msgstr empty, or the old rendered text is <20% CJK |
| Heavy rewrite of a translation | **two blocks**: red「修改前」above green「修改後」 | text ≥30 chars and >50% of characters changed |

Two blocks are used where a character diff would be solid red and green. Short text, such as
headings and table cells, always stays inline. Force a style with `--mode inline|blocks`, or
tune the rewrite cut-off with `--rewrite-threshold` (default 0.5). Each report line names the
mode used, e.g. `[blocks: rewritten, 87% changed]`.

## Run it

From the repo root:

```bash
uv run --no-project --with polib --with beautifulsoup4 --with playwright --with pillow \
  python .claude/skills/review-rendered-diff/scripts/render_diff.py howto/logging.po --base origin/3.15
```

| Flag | Default | Use |
|---|---|---|
| `--base` | `origin/3.15` | "before" version (fetch it first; SSH may fail, see below) |
| `--new` | working-tree file | "after" version as a git ref, e.g. a PR branch |
| `--out` | `.render-review/<po without .po>/` | where screenshots and builds go; with several POs, one subfolder per PO |
| `--context` | `140` | px of surrounding page kept above/below each paragraph |

Common targets:

| Review | Command arguments |
|---|---|
| Uncommitted edits | `<po> --base HEAD` |
| A PR branch | `<po> --base origin/3.15 --new <branch>` |
| One past commit, all its POs | `$(git show --name-only --format= <sha> -- '*.po') --base <sha>^ --new <sha>` |

Each PO takes about 40 seconds, because the page is built twice. The script prints one
line per changed entry (`L<entry line>: diff-N.png`), plus the diff page path and
`all-diffs.png`.

Before reporting, open a couple of PNGs with Read. To share them, use SendUserFile on
`all-diffs.png` if you have it. As a subagent, return the absolute paths instead. Or drag
the images into a GitHub comment.

## How it works (why it is safe)

- **Isolated builds:** each version's PO goes into its own temp `locale_dirs`, and
  `sphinx-build` runs on that one `.rst` into `--out/build-{old,new}/`. The working-tree PO
  and `../cpython/Doc/locales` are never touched.
- **Changed entries** are found by comparing msgstr per `(msgctxt, msgid)` with polib. A fuzzy
  msgstr counts as untranslated, because Sphinx does not render it, so a fixed fuzzy entry
  shows as a new translation.
- **Locating paragraphs:** roles, inline literals and links are dropped first, because
  `` :meth:`~Handler.setFormatter` `` renders as `setFormatter()`. The longest remaining plain
  run is matched against the rendered text, and the smallest enclosing block is used. When
  that run appears in several blocks (e.g. the `asdict()`/`astuple()` sentences), the block
  not yet highlighted and closest to the whole entry wins.
- **Two blocks in tables and lists** go inside the cell or item, so the table and list
  structure survives.
- **Diff on text, not HTML:** a character diff of the rendered text, applied to text nodes only,
  so links, inline code and `¶` anchors keep working.

## Gotchas

- **Do not use `make build` for this.** It hard-links the PO into `../cpython`, runs
  `git pull` on cpython, and swapping the PO in place risks losing uncommitted edits.
- **Exit code 1 is normal.** Sphinx fails on unrelated CPython redirect warnings
  (`library/functions.html redirects to ...`). The script judges success by whether the HTML
  exists. On failure, read `build-*/build.log`.
- **`SKIPPED (paragraph not found)`** means the entry has no rendered paragraph, e.g. an index
  entry or code block, or its msgid no longer matches the `../cpython` sources (the page
  shows English). Check `../cpython` is on the same branch as the PO. `../cpython` can also be
  newer than the PO's last CPython sync: those entries are not a script bug, they will turn
  fuzzy at the next sync, and are worth telling the PR author about. A trailing ` ::`
  literal-block marker is already handled, so it is not the cause. For a skip you cannot
  explain, grep the new msgstr's plain text in `build-new/html/<po>.html`.
- **A paragraph containing several changed entries** is highlighted once, and later entries
  report "already highlighted".
- **Inline diffs fragment small CJK edits** (e.g. 可能~~不是~~ shows only the changed
  characters). That is accurate. If a reviewer finds a paragraph choppy, rerun with
  `--mode blocks` or a lower `--rewrite-threshold`.
- **Do not judge a rewrite by `SequenceMatcher.ratio()`.** Common CJK characters keep
  matching, so a fully rewritten paragraph still scored 0.45. The script measures the share
  of changed characters instead.
- **A large new translation** (a whole file) makes one screenshot per paragraph, e.g. 147 for
  `howto/logging.po`. Point reviewers to `<po>-diff.html` rather than `all-diffs.png`.
- **Labels use the entry's first line** (the `#:` comment), not the msgstr line.
- **No `../cpython`:** run `make prepare_deps` once.
- **SSH to GitHub resets:** fetch over HTTPS:
  `git -c credential.helper='!gh auth git-credential' fetch https://github.com/python/python-docs-zh-tw.git 3.15:refs/remotes/origin/3.15`

## Not for

- Checking reST validity: use `make lint` / `sphinx-lint`.
- Judging translation quality: use the `validate-translation` skill. This skill only
  visualizes changes.
