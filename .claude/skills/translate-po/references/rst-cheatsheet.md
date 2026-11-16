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

`\\ ` (backslash-backslash-space) is a zero-width separator. It is needed where
reST requires a boundary but no visible space is wanted (see the table below
for when a plain space is the right choice instead):

### CJK Before Role (only if the role renders Chinese)
```
# Wrong
參閱:mod:`os`模組

# Correct
參閱 :mod:`os` 模組
```

### CJK After Link
```
# Wrong
`連結 <url>`_中

# Correct
`連結 <url>`_\\ 中
```

### Rendered Text Decides: `\\ ` or a Space

`\\ ` renders as nothing, so it removes the space the CJK-Latin rule requires.
Choose by what the role *renders*, not by how the source looks:

| Role renders | Use | Example |
|--------------|-----|---------|
| Chinese (`:term:` with a translated display text) | `\\ ` | `包含\\ :term:`擴充模組 <extension module>`\\ 的套件` |
| Latin (`:ref:`/`:doc:` with no explicit title, which shows the target's English section title; `:mod:`, `:func:`, `:class:`, etc.) | a plain space | `請參閱 :ref:`threadsafety`。` |

```
# Wrong: renders "請參閱C API Extension Support for Free Threading"
請參閱\\ :ref:`freethreading-extensions-howto`。

# Correct: renders "請參閱 C API Extension Support for Free Threading"
請參閱 :ref:`freethreading-extensions-howto`。
```

For `:ref:`/`:doc:` without an explicit title, the rendered text is the
target page's title, which is often still English, so check the rendered page.
A role with a translated title (`:ref:`詳細說明 <detail-section>``) renders
Chinese, so `\\ ` applies.

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
