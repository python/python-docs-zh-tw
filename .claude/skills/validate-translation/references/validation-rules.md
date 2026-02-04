# Validation Rules

Complete checklist for reviewing translations.

## Structural Checks

| Check | Severity | Description |
|-------|----------|-------------|
| Empty msgstr | ERROR | Translation missing |
| msgid modified | ERROR | Source text was changed (never modify) |
| Invalid PO syntax | ERROR | Malformed PO entry |
| Obsolete entry | WARNING | Entry marked obsolete |

## Punctuation Checks

| Check | Severity | Pattern |
|-------|----------|---------|
| Half-width in Chinese | ERROR | `,` `.` `;` `:` in Chinese text |
| Full-width in English | WARNING | `，` `。` `；` `：` in English text |
| Mismatched quotes | ERROR | `「` without `」` or vice versa |
| Mismatched parens | ERROR | `（` without `）` or vice versa |

### Punctuation Rules

**Chinese text uses:**
- Quotes: `「」`（single）`『』`（nested）
- Parentheses: `（）`
- Comma: `，`
- Period: `。`
- Colon: `：`
- Semicolon: `；`
- Exclamation: `！`
- Question: `？`
- List separator: `、`

**English text uses:**
- Standard ASCII punctuation

## Spacing Checks

| Check | Severity | Pattern |
|-------|----------|---------|
| Missing CJK-Latin space | WARNING | Chinese directly adjacent to Latin |
| Extra space | INFO | Multiple consecutive spaces |
| Trailing space | WARNING | Space at end of line |

### Correct Examples
- `"使用 CPU 運算"` - space between CJK and Latin
- `"使用「CPU」運算"` - no space with symbols

## Line Length Checks

| Check | Severity | Threshold |
|-------|----------|-----------|
| Line too long | ERROR | > 79 characters |
| Inefficient wrapping | INFO | Could be better wrapped |

## reST Syntax Checks

| Check | Severity | Description |
|-------|----------|-------------|
| Role broken | ERROR | `:role:` syntax malformed |
| Link broken | ERROR | Link syntax malformed |
| Missing backslash | WARNING | CJK adjacent to role without `\\ ` |
| Directive changed | ERROR | Directive name/args modified |
| URL modified | ERROR | Link URL was changed |
| `::` marker removed | ERROR | Code block marker deleted |

## Terminology Checks

| Check | Severity | Description |
|-------|----------|-------------|
| Forbidden zh_CN term | ERROR | Uses Simplified Chinese term |
| Wrong glossary term | WARNING | Term differs from glossary |
| Inconsistent term | WARNING | Same term translated differently |

### Top Forbidden Terms (zh_CN -> zh_TW)

| Forbidden | Required |
|-----------|----------|
| 函數 | 函式 |
| 返回 | 回傳 |
| 對象 | 物件 |
| 迭代 | 疊代 |
| 創建 | 建立 |
| 代碼 | 程式碼 |
| 信息 | 資訊 |
| 異常 | 例外 |
| 默認 | 預設 |
| 調用 | 呼叫 |

## Output Format

Report validation results in this format:

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

## Validation Commands

```bash
make lint              # sphinx-lint for reST
make wrap              # powrap for line length
make build <file>.po   # Test Sphinx build
make all               # Full documentation build
```
