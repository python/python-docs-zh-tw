---
name: validate-translation
description: Validate translated PO entries against project rules, terminology, and reST syntax. Use after translating or reviewing translations.
metadata:
  short-description: Validate translation quality
---

# validate-translation

## Scope
- Validate existing translations in PO files
- Check formatting, punctuation, spacing, and terminology rules
- Report errors, warnings, and suggestions
- Ensure reST syntax preservation

## Validation Checklist

### 1. Structural Checks
| Check | Severity | Description |
|-------|----------|-------------|
| Empty msgstr | ERROR | Translation missing for non-fuzzy entry |
| msgid modified | ERROR | Source text was incorrectly changed |
| Invalid PO syntax | ERROR | Malformed PO entry structure |

### 2. Punctuation Checks
| Check | Severity | Rule |
|-------|----------|------|
| Half-width in Chinese | ERROR | Chinese text must use `，。；：！？「」（）` |
| Full-width comma/period in English | WARNING | English text should use `,.;:!?()` |
| Mismatched quotes | ERROR | `「` must pair with `」` |
| Mismatched parentheses | ERROR | `（` must pair with `）` |

### 3. Spacing Checks
| Check | Severity | Rule |
|-------|----------|------|
| Missing CJK-Latin space | WARNING | Add space between Chinese and English text |
| No space before/after symbols | OK | `使用「CPU」運算` is correct |
| Trailing whitespace | WARNING | No trailing spaces in msgstr |

### 4. Line Length
| Check | Severity | Threshold |
|-------|----------|-----------|
| Line too long | ERROR | > 79 characters per line |

### 5. reST Syntax Checks
| Check | Severity | Description |
|-------|----------|-------------|
| Role syntax broken | ERROR | `:role:`content`` malformed |
| Role name changed | ERROR | Role type was modified |
| Link target changed | ERROR | URL or reference target modified |
| Missing backslash escape | WARNING | CJK adjacent to role needs `\\ ` |

### 6. Terminology Checks
| Check | Severity | Description |
|-------|----------|-------------|
| zh_CN term used | WARNING | Simplified Chinese variant detected |
| Inconsistent term | WARNING | Same term translated differently |
| High-freq term translated | INFO | Terms like `int`, `list` should stay English |

### 7. Context-Dependent Decisions
| Check | Severity | Description |
|-------|----------|-------------|
| Reviewer context rule | INFO | If a reviewer decides a term/pattern depends on nearby context, record it in the Context Decision Log in `terminology-check` for future reference. |

## Validation Process

1. **Read the PO entry** - Parse msgid, msgstr, comments, and flags
2. **Check structure** - Verify PO syntax is valid
3. **Check punctuation** - Apply Chinese/English punctuation rules
4. **Check spacing** - Verify CJK-Latin spacing
5. **Check line length** - Ensure <= 79 characters
6. **Check reST** - Validate roles, links, escaping
7. **Check terminology** - Cross-reference with glossary and Context Decision Log
8. **Record context rules** - If a decision depends on nearby context, add it to the Context Decision Log

## Output Format

```
=== Validation: library/functions.po ===

Entry #42 (line 156):
  msgid: "This function returns an iterator."
  msgstr: "此函數返回一個迭代器。"

  [ERROR] Terminology: "函數" should be "函式"
  [WARNING] Terminology: "返回" should be "回傳"
  [WARNING] Terminology: "迭代器" should be "疊代器"

Summary: 1 error, 2 warnings
```

## Common Fixes

| Issue | Before | After |
|-------|--------|-------|
| zh_CN term | 函數 | 函式 |
| zh_CN term | 返回 | 回傳 |
| zh_CN term | 對象 | 物件 |
| Missing space | 使用CPU | 使用 CPU |
| Wrong punctuation | 例如, | 例如， |
| Missing escape | 參閱:mod:`os` | 參閱\\ :mod:`os` |

## Related Skills
- `doc-translate` - General translation rules
- `rst-translate` - reST-specific rules
- `terminology-check` - Detailed terminology validation
