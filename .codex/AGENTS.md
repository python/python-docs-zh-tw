# Repository Guidelines

## Project Structure & Module Organization
This repo contains Traditional Chinese translations of the Python docs. The
content is organized as `.po` files at the root and within topic folders such
as `library/`, `tutorial/`, `reference/`, `c-api/`, and `using/`. Terminology
references live in `glossary.po`, and overall workflow guidance is in
`README.rst`. There is no application source code; most changes are to `.po`
files and translation metadata.

## Build, Test, and Development Commands
- `make all` builds the full docs with Sphinx and validates rST syntax. It may
  clone CPython into a sibling `../cpython` directory if missing.
- `make lint` runs a quick rST syntax check without a full build.
- `make build path/to/file.po` builds a single translation file (faster for
  spot-checking).
- `pre-commit install` enables PO-format checks at commit time (recommended).

## Coding Style & Naming Conventions
- Only edit `msgstr`; do not change `msgid`.
- Keep PO lines <= 79 chars (Poedit or `powrap` can wrap).
- Preserve rST roles, directives, and link targets exactly.
- Follow the project glossary and translation rules (see `glossary.po` and the
  project wiki).
- Branch names typically mirror the file path, e.g., `library/math`.

## Testing Guidelines
There is no unit test suite. Validate changes by running `make lint` or
`make all` and ensuring there are no warnings. If you build a specific file,
confirm the generated HTML in `../cpython/Doc/build/html`.

## Commit & Pull Request Guidelines
- Open an issue to claim a translation task before starting.
- Base your branch on `upstream/3.13`.
- Use clear commit messages; the repo example is
  `Working on path/to/file.po`.
- In PRs, summarize the files translated, link the issue, and note any build
  checks you ran (e.g., `make lint`).

## Agent-Specific Instructions

### Available Skills
Use these skills located in `.claude/skills/` and project root:

| Skill | Location | When to Use |
|-------|----------|-------------|
| `doc-translate` | `doc-translate/SKILL.md` | General EN->zh_TW translation rules |
| `rst-translate` | `rst-translate/SKILL.md` | Strings with reST syntax |
| `translate-po` | `.claude/skills/translate-po.md` | Core translation workflow |
| `validate-translation` | `.claude/skills/validate-translation.md` | After translating, validate quality |
| `terminology-check` | `.claude/skills/terminology-check.md` | Check terminology consistency |

### Translator Agent
**Purpose:** Translate PO file entries with full context awareness.

**Workflow:**
1. Read the target PO file and identify untranslated entries
2. For each entry, use `translate-po` skill
3. Apply `terminology-check` for consistency
4. Validate with `validate-translation`
5. Save with proper formatting (79 char lines)

**Invocation:** When asked to translate a PO file or entries.

### Reviewer Agent
**Purpose:** Review existing translations, especially fuzzy entries.

**Workflow:**
1. Find fuzzy entries with `make fuzzy` or grep for `#, fuzzy`
2. For each fuzzy entry:
   - Compare msgid changes (check translator comments)
   - Update msgstr to match new msgid
   - Apply `terminology-check` for zh_CN variants
   - Validate with `validate-translation`
3. Remove fuzzy flag after review
4. Run `make lint` to verify

**Invocation:** When asked to review translations or fix fuzzy entries.

### Quality Agent
**Purpose:** Comprehensive quality assurance for translations.

**Workflow:**
1. Run `validate-translation` on target files
2. Run `terminology-check` for consistency
3. Check reST syntax with `make lint`
4. Generate quality report with issues found
5. Prioritize fixes by severity (ERROR > WARNING > INFO)

**Invocation:** When asked to check translation quality or before PR.

## Quick Reference

### Translation Rules Summary
- Chinese: full-width punctuation `「」（）、，。`
- English: half-width punctuation `(),.;:!?`
- Spacing: add space between CJK and Latin text
- Lines: max 79 characters
- High-freq terms stay English: `int`, `str`, `list`, `dict`, `iterator`, `generator`

### Common zh_CN -> zh_TW Fixes
```
函數 -> 函式    對象 -> 物件    返回 -> 回傳
模塊 -> 模組    字符串 -> 字串   迭代 -> 疊代
調用 -> 呼叫    內存 -> 記憶體   異步 -> 非同步
```

### reST Escaping
```
CJK before role:  參閱\\ :mod:`os`
CJK after link:   `連結 <url>`_\\ 中
```
