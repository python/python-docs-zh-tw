---
name: rst-translate
description: Use when translating strings that include reStructuredText (rST) syntax in this repo.
metadata:
  short-description: rST translation rules
---

# rst-translate

## Scope
- Apply rST-specific spacing, escaping, and formatting rules during translation.
- Preserve all rST roles, directives, and link targets exactly.

## Double Backslash Usage (\\)
Use `\\` to preserve rST-required spacing without rendering a visible space in HTML.

### When spaces are required for rST parsing
```text
參閱 :mod:`os` 模組
```
```text
參閱\\ :mod:`os` 模組
```

### When rST renders Chinese text
```text
一個 :term:`file object`。
一個\\ :term:`檔案物件 <file object>`。
參考 `wiki 文章 <https://wiki.com/...>`_\\ 中
```

## Common rST Edge Cases
Fullwidth punctuation (，。： etc.) is fine with rST roles:
```text
一個 :term:`file object`。
```

Fullwidth parentheses require escaping:
```text
一個 :term:`file object`（   # build failed
一個 :term:`file object`\\（
```

## Link Display Text
For inline links with explicit titles, translate the visible text and keep the URL unchanged.
```text
`specification for packages <https://www.python.org/doc/essays/packages/>`_
`套件規格 <https://www.python.org/doc/essays/packages/>`_
```

For :ref: with explicit titles, translate the visible text and keep the target unchanged.
```text
:ref:`the remaining cases <using-on-interface-options>`
:ref:`其餘情況 <using-on-interface-options>`
```

For :term: with explicit titles, translate the visible text and keep the target unchanged.
```text
:term:`namespace packages <namespace package>`
:term:`命名空間套件 <namespace package>`
```

## Literal Block Marker (::)
When source ends with `::`, translate to keep `::` while using a fullwidth colon:
```text
msgid "blah blah::"
msgstr "blah blah： ::"
```
