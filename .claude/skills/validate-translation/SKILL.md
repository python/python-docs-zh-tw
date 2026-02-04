---
name: validate-translation
description: Reviews translated PO entries for quality, checking terminology, punctuation, reST syntax, and line length. Use to validate existing translations.
argument-hint: <path-to-po-file>
---

# review-translation

Validate translated PO entries against project rules and report issues.

## What to Check

### 1. Terminology Consistency
- Compare terms against `glossary.po` and terminology dictionary
- Flag zh_CN terms that should be zh_TW (see `references/validation-rules.md`)
- Check for inconsistent translations of the same term

### 2. Punctuation Rules
- Chinese text must use full-width: `「」（）、，。：；！？`
- English text must use half-width: `(),.;:!?`
- Brackets: Full-width if content has Chinese, half-width if English-only

### 3. CJK-Latin Spacing
- Space required between Chinese and Latin characters
- No space between Latin and Chinese punctuation/symbols

### 4. reST Syntax Preservation
- All `:role:` syntax must be intact
- Link URLs must be unchanged
- `::` markers must be preserved
- Check for missing `\\ ` escapes before roles

### 5. Line Length
- Maximum 79 characters per line
- Multi-line format for longer content

## Review Process

1. **Parse PO file** - Extract msgid/msgstr pairs
2. **Check each entry** - Apply all validation rules
3. **Categorize issues** - ERROR (must fix), WARNING (should fix), INFO
4. **Generate report** - List issues with line numbers and suggestions

## Issue Severity

| Severity | Description | Examples |
|----------|-------------|----------|
| ERROR | Must fix before merge | Broken reST, missing translation |
| WARNING | Should fix | Wrong terminology, spacing issues |
| INFO | Optional improvement | Inefficient line wrapping |

## Quick Validation Commands

After review, run: `make lint`, `make wrap`, `make build <file>.po`

## References

- `references/validation-rules.md` - Complete validation checklist
