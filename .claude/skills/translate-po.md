---
name: translate-po
description: Core skill for translating PO file entries from English to Traditional Chinese. Orchestrates doc-translate, rst-translate, and terminology-check.
metadata:
  short-description: Translate PO entries EN->zh_TW
---

# translate-po

## Scope
- Translate English PO msgid entries to Traditional Chinese msgstr
- Apply all formatting, punctuation, and spacing rules
- Preserve reStructuredText syntax exactly
- Maintain terminology consistency with glossary
- Mark uncertain translations with fuzzy flag

## Prerequisites

Before translating, always:
1. Read the full msgid to understand context
2. Check msgctxt for additional context if present
3. Review translator comments (#. and #:)
4. Look up unfamiliar terms in glossary references

## Translation Workflow

### Step 1: Analyze Content Type

Identify what you're translating:
- **Pure prose** - No markup, straightforward translation
- **Code-only** - Preserve exactly, do not translate
- **Mixed** - Prose with inline code/roles (most common)
- **reST structural** - Directives, links, complex markup

### Step 2: Apply Translation Rules

#### Punctuation
```
Chinese sentences -> Full-width: 「」（）、，。：；！？
English sentences -> Half-width: (),.;:!?
```

#### Spacing
```
Add space between CJK and Latin: 使用 CPU 運算
No space with symbols: 使用「CPU」運算
```

#### Terminology
- Use `terminology-check` skill for reference
- High-frequency terms stay English: int, float, str, list, tuple, dict, iterator, generator
- Follow glossary for standard terms

### Step 3: Handle reST Syntax

Use `rst-translate` skill rules:

#### Roles - Keep syntax, translate display text if needed
```
:mod:`os`                    -> :mod:`os` (unchanged)
:term:`iterator`             -> :term:`疊代器 <iterator>`
:ref:`section-name`          -> :ref:`章節名稱 <section-name>`
```

#### Backslash Escaping
```
CJK before role:   參閱\\ :mod:`os`
CJK after link:    `連結 <url>`_\\ 中
Full-width after:  :term:`object`\\（
```

#### Literal Blocks
```
msgid "Example::"
msgstr "範例： ::"
```

### Step 4: Format Output

#### Line Wrapping (max 79 chars)
```
msgstr ""
"第一行翻譯內容"
"第二行繼續翻譯。"
```

#### Fuzzy Flag
Add `#, fuzzy` when:
- Translation is uncertain
- Machine-translated content
- Needs human review

```
#, fuzzy
msgid "Original text"
msgstr "可能需要審核的翻譯"
```

## Quality Checklist

Before finalizing, verify:
- [ ] Line length <= 79 characters
- [ ] Punctuation rules followed (full-width for Chinese)
- [ ] Spacing rules followed (space between CJK/Latin)
- [ ] reST syntax preserved exactly
- [ ] Terminology consistent with glossary
- [ ] No empty msgstr (unless intentionally skipping)

## Examples

### Simple Prose
```
msgid "Python is a programming language."
msgstr "Python 是一種程式語言。"
```

### With Terminology
```
msgid "This function returns an iterator."
msgstr "此函式回傳一個疊代器。"
```

### With reST Role
```
msgid "See :func:`len` for details."
msgstr "詳情請參閱\\ :func:`len`。"
```

### With Link
```
msgid "Visit the `Python website <https://python.org>`_."
msgstr "請造訪 `Python 網站 <https://python.org>`_。"
```

### With Term Reference
```
msgid "Returns a :term:`context manager`."
msgstr "回傳一個\\ :term:`情境管理器 <context manager>`。"
```

### Mixed Content
```
msgid "The :class:`list` type is a :term:`mutable` sequence."
msgstr ":class:`list` 型別是一個\\ :term:`可變物件 <mutable>` 序列。"
```

## Related Skills
- `doc-translate` - General translation rules
- `rst-translate` - reST-specific rules
- `terminology-check` - Terminology validation
- `validate-translation` - Post-translation validation

## References
- Terminology: `doc-translate/references/terminology.md`
- Glossary: `glossary.po`
- Wiki: https://github.com/python/python-docs-zh-tw/wiki/術語列表
