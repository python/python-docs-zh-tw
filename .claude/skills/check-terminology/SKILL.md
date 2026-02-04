---
name: check-terminology
description: Checks terminology consistency against project glossary and identifies zh_CN terms that need conversion to zh_TW. Use to verify term usage.
argument-hint: <term-or-po-file>
---

# check-terminology

Check terminology against project glossary and zh_CN/zh_TW mappings.

## Terminology Sources

1. **Primary:** `glossary.po` - Official Python glossary translations
2. **Secondary:** `focused_terminology_dictionary.csv` - 118 key terms
3. **Tertiary:** `.scripts/google_translate/utils.py` - zh_CN to zh_TW mappings

## Check Process

### For a Single Term
1. Search in `../translate-po/references/terminology.md`
2. Check if it's in `references/keep-in-english.md`
3. If found, use the standard translation
4. If not found, check `glossary.po` in project root

### For a PO File
1. Extract all translated terms from msgstr
2. Cross-reference against glossary
3. Identify forbidden zh_CN terms
4. Report inconsistencies

## Error Categories

### Category 1: Forbidden Terms (Must Fix)
zh_CN terms that must be converted to zh_TW.

Example violations:
- `函數` -> should be `函式`
- `返回` -> should be `回傳`
- `對象` -> should be `物件`

### Category 2: Inconsistent Terms (Should Review)
Same English term translated differently across files.

### Category 3: Missing from Glossary (Informational)
New terms not yet in the glossary.

## Context Decision Log

When a reviewer decides a translation depends on nearby context (above/below),
record the decision here for future reference. Keep entries short and specific.

Format:
- **Term/pattern:** ...
- **Decision:** ...
- **Context cue:** ...
- **Example:** `source` -> `translation`

Example:
- **Term/pattern:** 類型 / 型別
- **Decision:** 用語依上下文；Python 型別物件用「型別」，一般分類用「類型」
- **Context cue:** 出現 `int/str/dict/type` 或 "type object"
- **Example:** "two types of packages" -> "兩種類型的套件"

Decision Log:
- **Term/pattern:** 類型 / 型別
- **Decision:** 用語依上下文；Python 型別物件用「型別」，一般分類用「類型」
- **Context cue:** 出現 `int/str/dict/type` 或 "type object"
- **Example:** "two types of packages" -> "兩種類型的套件"

## Quick Lookup

1. Check `../translate-po/references/terminology.md` first (authoritative, 186 terms)
2. If term should stay in English, see `references/keep-in-english.md`

## References

- `../translate-po/references/terminology.md` - Complete term translations (186 terms)
- `references/keep-in-english.md` - Terms that stay in English
