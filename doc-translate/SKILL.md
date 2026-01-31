---
name: doc-translate
description: Use when translating English content to Traditional Chinese in this repo (python-docs-zh-tw), especially for PO/reStructuredText content.
metadata:
  short-description: Translate EN to zh-tw for docs
---

# doc-translate

## Scope
- Translate English documentation to Traditional Chinese for this repo.
- Preserve reStructuredText/PO formatting and links exactly.

## Workflow
1) Read the full source section before translating to preserve meaning and context.
2) Translate with the rules below; keep PO syntax intact.
3) Check line length (PO), spacing, and punctuation rules.
4) Confirm glossary terms and high-frequency words are handled as specified.

## Translation Rules
- Chinese sentences use fullwidth punctuation; English sentences keep halfwidth punctuation.
  - Example: 「」（）、，。
  - Example: Python is supported by Python Software Foundation (PSF).
- Mixed Chinese/English should include spaces between Chinese and English words; no extra space between English words and symbols.
  - Example: 使用 CPU 運算、使用「CPU」運算
- Proper nouns should follow the glossary translation when available.
- Proper nouns may remain untranslated (e.g., CPU, Unicode).
- For uncommon or uncertain terms, add a parenthetical note or keep the original term; annotate only on first occurrence per page.
  - Example: 正規表示式 (regular expression)
  - Example: Network News Transfer Protocol、Portable Network Graphics（可攜式網路圖形）
- PO lines should be <= 79 characters (Poedit handles this; `powrap` is optional).
- High-frequency terms should stay in English (even if glossary includes a translation).
  - Example: int, float, str, bytes, list, tuple, dict, set, iterator, generator, iterable, pickle

## Parentheses
- If parentheses contain Chinese, use fullwidth parentheses.
- If parentheses contain only English, use halfwidth parentheses and keep English spacing.
  - Example: list（串列）是 Python 中很常見的資料型別。
  - Example: 在本情況使用 zip(*[iter(x)]*n) 是很常見的情況（Python 慣例）。
  - Example: 在超文件標示語言 (HTML) 中應注意跳脫符號。

## Related Skills
- Use `rst-translate` when the string includes reStructuredText syntax.

## References
- Local glossary: `glossary.po`
- Terminology excerpt: `doc-translate/references/terminology.md`
- Term list (wiki): https://github.com/python/python-docs-zh-tw/wiki/%E8%A1%93%E8%AA%9E%E5%88%97%E8%A1%A8
- Official glossary: https://docs.python.org/zh-tw/3/glossary.html
