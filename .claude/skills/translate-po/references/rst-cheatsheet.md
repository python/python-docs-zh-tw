# reST Syntax Cheatsheet

Rules for preserving reStructuredText syntax in translations.

## Common Roles

| Role | Purpose | Example |
|------|---------|---------|
| `:mod:` | Module reference | `:mod:`os`` |
| `:func:` | Function reference | `:func:`len`` |
| `:class:` | Class reference | `:class:`list`` |
| `:meth:` | Method reference | `:meth:`str.split`` |
| `:attr:` | Attribute reference | `:attr:`__name__`` |
| `:data:` | Data reference | `:data:`sys.path`` |
| `:const:` | Constant reference | `:const:`True`` |
| `:term:` | Glossary term | `:term:`iterator`` |
| `:ref:` | Cross-reference | `:ref:`section-name`` |
| `:pep:` | PEP reference | `:pep:`8`` |
| `:exc:` | Exception reference | `:exc:`ValueError`` |
| `:doc:` | Document reference | `:doc:`tutorial/index`` |

## Role Translation Rules

### Keep Unchanged
```
:mod:`os`  ->  :mod:`os`
:func:`len`  ->  :func:`len`
:exc:`ValueError`  ->  :exc:`ValueError`
```

### Translate with Target
```
:term:`iterator`  ->  :term:`疊代器 <iterator>`
:term:`namespace packages <namespace package>`  ->  :term:`命名空間套件 <namespace package>`
:ref:`detail-section`  ->  :ref:`詳細說明 <detail-section>`
:ref:`the remaining cases <using-on-interface-options>`  ->  :ref:`其餘情況 <using-on-interface-options>`
```

## Backslash Escaping

Use `\\ ` (backslash-backslash-space) as zero-width separator:

### CJK Before Role
```
# Wrong
參閱:mod:`os`模組

# Correct
參閱\\ :mod:`os` 模組
```

### CJK After Link
```
# Wrong
`連結 <url>`_中

# Correct
`連結 <url>`_\\ 中
```

### Full-width Punctuation After Role
```
# May break build
:term:`object`（

# Correct
:term:`object`\\（
```

## Link Syntax

```
# Original
`Python website <https://python.org>`_

# Translated (keep URL, translate display)
`Python 網站 <https://python.org>`_
```

## Code Block Markers

The `::` marker introduces a code block:

```
# Original
Here is the code::

# Translated (use fullwidth colon before ::)
程式碼如下： ::
```

When source ends with `::`, translate to keep `::` while using a fullwidth colon:
```
msgid "blah blah::"
msgstr "blah blah： ::"
```

## Literal Blocks

Preserve indentation and content exactly. Only translate comments if needed.

## Multi-line Format

For long translations, use PO multi-line format:
```
msgstr ""
"第一行的翻譯內容 "
"延續到第二行。"
```

Each line must be <= 79 characters including quotes.
