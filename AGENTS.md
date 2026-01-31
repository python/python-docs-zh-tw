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
- Use the local skills when translating: `doc-translate/` for general rules
  and `rst-translate/` when strings include rST syntax.
