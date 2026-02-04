# Python Documentation Traditional Chinese Translation

This project translates Python 3.14 official documentation to Traditional Chinese (zh_TW).

## Build Commands

```bash
make all              # Build all documentation
make build <file>.po  # Build single file (e.g., make build howto/logging.po)
make lint             # Check reST syntax with sphinx-lint
make wrap             # Format PO files with powrap (max 79 chars)
make fuzzy            # List entries marked as fuzzy
make progress         # Check translation progress
```

## Translation Conventions

### Punctuation
- **Chinese text:** Full-width punctuation - 「」（）、，。：；！？
- **English text:** Half-width punctuation - (),.;:!?

### CJK-Latin Spacing
- Add space between Chinese and Latin: "使用 CPU 運算" (correct)
- No space when adjacent to symbols: "使用「CPU」運算" (correct)

### Terminology
- class -> 類別 | function -> 函式 | method -> 方法
- module -> 模組 | argument -> 引數 | parameter -> 參數
- decorator -> 裝飾器 | iterator -> 疊代器

### Keep in English
`int`, `float`, `str`, `bytes`, `list`, `tuple`, `dict`, `set`, `iterator`, `generator`, `pickle`

### reST Syntax
- Preserve `:mod:`, `:func:`, `:class:`, `:term:`, `:ref:`, `:pep:` roles
- Use `\\ ` as zero-width separator when Chinese precedes reST syntax

## Key Resources

- **Terminology:** `focused_terminology_dictionary.csv`, `glossary.po`
- **zh_CN corrections:** `.scripts/google_translate/utils.py`
- **Full guidelines:** `README.rst` (lines 240-377)
- **Skills:** `.claude/skills/` for detailed translation workflows
