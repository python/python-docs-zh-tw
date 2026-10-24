---
name: review-rendered-html
description: Builds translated PO files into HTML and reviews the rendered page for reading flow and formatting, by reading the extracted page text and checking Playwright screenshots. Use after translating or editing a PO file, before opening a PR.
argument-hint: <po-file> [<po-file> ...]
---

# review-rendered-html

PO-level checks (`msgfmt`, `make lint`, terminology) cannot show how a
translation reads on the published page. reST roles disappear, links and
literals change spacing, and Sphinx adds its own labels. Review the rendered
HTML of every page you changed before opening a PR.

## Prerequisites

- CPython clone at `../cpython` on the branch matching `VERSION` in the
  Makefile, and the docs venv (`make prepare_deps` sets up both)
- Playwright MCP tools (`browser_navigate`, `browser_take_screenshot`) for
  screenshots; without them, read the text dump only and say so in the report

## Step 1: Build and dump the rendered text

```bash
python3 .scripts/render_review.py library/dataclasses.po [faq/library.po ...]
```

- Builds only the given pages (same Sphinx options as `make build`) and writes
  the page prose, without code blocks, to `.render-review/<page>.txt`
- Prints heuristic findings with the line in the text dump; `--no-build`
  re-checks without rebuilding
- "build reported problems" about `redirects to builtins/...` comes from a
  reused build directory and does not affect the page

## Step 2: Read the text dump as a reader

Read `.render-review/<page>.txt` end to end, focusing on paragraphs from the
entries you changed. For each one check:

- **Flow:** the sentence reads as natural Taiwanese technical writing; no
  translationese (被…所…, 將會是, 除…之外的其他事項), no dangling clauses
  after a role's text disappears
- **Spacing:** one space between CJK and Latin/digits/literals; no space
  next to full-width punctuation; no stray space inside Chinese text
- **Punctuation:** full-width `，。：；（）「」` around Chinese; the colon before
  a code block stays `：`
- **Completeness:** compare with the English page when meaning is unclear

Confirm or dismiss every heuristic finding by reading its context. Findings in
entries you did not touch are follow-ups, not part of the current change.

Paragraphs still in English are usually not your bug. Either the entry is
untranslated, or the PO msgid is older than the CPython clone, because the
source changed after the last sync. Mention them in the report and don't fix
them in the PO by hand.

## Step 3: Screenshot and inspect the layout

Serve the build and open the sections you changed:

```bash
python3 -m http.server 8765 --bind 127.0.0.1 --directory ../cpython/Doc/build/html
```

Then use the Playwright MCP tools:

1. `browser_resize` to 1280x1600
2. `browser_navigate` to `http://127.0.0.1:8765/<page>.html#<anchor>`
3. `browser_take_screenshot` with `filename: ".playwright-mcp/<name>.png"`
   (the MCP only writes inside the repo; `.playwright-mcp/` is gitignored)
4. Read the PNG and check: links and `:term:` text sit flush with the Chinese
   around them, inline code has normal spacing, parameter lists, notes and
   admonitions keep their structure, and headings and the sidebar TOC show
   the translated titles

Stop the server when done.

## Common rendered-only problems and fixes

| Rendered | Cause in msgstr | Fix |
|---|---|---|
| `field可以` | ``` ``field``\ 可以 ``` | ``` ``field`` 可以 ``` (keep the space after a literal before CJK) |
| `全域直譯器鎖(GIL) 來` | `` :term:`…`\ (GIL) 來 `` | `` :term:`…`\ （GIL）來 `` (full-width parens, no extra space) |
| `磁碟區上的 替代資料串流` | `` 的 `替代資料串流 <url>`_ `` | `` 的\ `替代資料串流 <url>`_ `` |
| `:meth:` or backticks visible | role typo such as `:meth: ` with a space | restore the exact role syntax |
| `` `\ `` visible | escaped backslash doubled in the PO | one `\\ ` in the PO file (`\ ` in the value) |

A reST role or link must be followed by whitespace or ASCII/closing
punctuation, so a full-width opening bracket after a role still needs `\ `.

## Report

List per page: findings fixed, findings dismissed (with reason), follow-ups
in untouched entries, English paragraphs and their likely cause, and the
screenshots you checked.
