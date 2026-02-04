---
name: translate-po
description: Translates PO file entries from English to Traditional Chinese (zh_TW) following project conventions. Use when translating new PO files or untranslated entries.
argument-hint: <path-to-po-file>
---

# translate-po

Translate English PO msgid entries to Traditional Chinese msgstr following all project rules.

## Prerequisites

1. Read the full msgid before translating
2. Check msgctxt and translator comments for context
3. Look up terminology in `references/terminology.md`
4. Check `references/forbidden-terms.md` for zh_CN terms to avoid

## Translation Process

### Step 1: Content Analysis
Identify content type:
- **Pure prose:** Translate normally
- **Code-only:** Preserve exactly (no translation)
- **Mixed:** Translate prose, preserve code/roles
- **reST structural:** Preserve directives, translate display text

### Step 2: Apply Rules

**Punctuation:**
- Chinese text: Full-width `「」（）、，。：；！？`
- English text: Half-width `(),.;:!?`

**CJK-Latin Spacing:**
- Add space between Chinese and Latin: "使用 CPU 運算" (correct)
- No space with symbols: "使用「CPU」運算" (correct)

**Line Width:** Max 79 characters (use multi-line format for longer text)

### Step 3: reST Handling

See `references/rst-cheatsheet.md` for complete rules.

**Key patterns:**
- `:mod:`os`` -> Keep unchanged
- `:term:`iterator`` -> `:term:`疊代器 <iterator>``
- Chinese before role: "參閱\\ :mod:`os`"
- After `::` markers: "範例： ::"

### Step 4: Terminology Workflow

1. Check term in `references/terminology.md`
2. If not found, check `glossary.po` in project root
3. If uncertain, add `#, fuzzy` flag
4. Never use zh_CN terms from `references/forbidden-terms.md`

## Output Format

```
msgid "Original English text"
msgstr "翻譯後的中文內容"
```

For uncertain translations, add `#, fuzzy` flag before the entry.

## Quality Checklist

Before outputting, verify:
- [ ] Line length <= 79 characters
- [ ] Full-width punctuation in Chinese text
- [ ] CJK-Latin spacing correct
- [ ] reST syntax preserved
- [ ] Terminology matches glossary
- [ ] No forbidden zh_CN terms

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

### Multi-line Format
```
msgstr ""
"第一行翻譯內容"
"第二行繼續翻譯。"
```

### Fuzzy Flag
Add `#, fuzzy` when translation is uncertain or needs human review:
```
#, fuzzy
msgid "Original text"
msgstr "可能需要審核的翻譯"
```

## References

- `references/terminology.md` - Key term translations (186 terms)
- `references/forbidden-terms.md` - zh_CN to zh_TW mappings
- `references/rst-cheatsheet.md` - reST syntax rules
