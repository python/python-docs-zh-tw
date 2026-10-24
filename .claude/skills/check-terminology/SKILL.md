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
4. **Usage evidence (not authority):** `.scripts/translation_memory.sh query "<term>"` - how existing translated .po entries render the term (skip if the command fails)
5. **Reviewer-enforced terms:** the "Terminology enforced by reviewers" table in `../translate-po/references/review-corrections.md` - pairs reviewers repeatedly corrected (e.g. 傳回→回傳, 您→你, 協議→協定, 運行→執行), some context-dependent (串列 vs 清單, 檔案 vs 文件)

## Check Process

### For a Single Term
1. Search in `../translate-po/references/terminology.md`
2. Check if it's in `references/keep-in-english.md`
3. If found, use the standard translation
4. If not found, check `glossary.po` in project root
5. Run `.scripts/translation_memory.sh query "<term>" --top-k 10` to see existing renderings with `path:line`; if the glossary is silent, report the dominant rendering as a suggestion

### For a PO File
1. Extract all translated terms from msgstr
2. Cross-reference against glossary
3. Identify forbidden zh_CN terms
4. For each term that looks inconsistent, run `.scripts/translation_memory.sh query "<English term>" --top-k 10` and compare renderings across files
5. Report inconsistencies, citing `path:line` from the lookup

## Error Categories

### Category 1: Forbidden Terms (Must Fix)
zh_CN terms that must be converted to zh_TW.

Example violations:
- `函數` -> should be `函式`
- `返回` -> should be `回傳`
- `對象` -> should be `物件`

### Category 2: Inconsistent Terms (Should Review)
Same English term translated differently across files.

Gather evidence with the translation memory lookup and cite each rendering with
`path:line`. The glossary decides; majority usage only informs a suggestion
when the glossary is silent.

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
3. To see how a term is actually rendered across files: `.scripts/translation_memory.sh query "<term>"`

## References

- `../translate-po/references/terminology.md` - Complete term translations (186 terms)
- `references/keep-in-english.md` - Terms that stay in English
- [術語列表 Wiki](https://github.com/python/python-docs-zh-tw/wiki/%E8%A1%93%E8%AA%9E%E5%88%97%E8%A1%A8) - Project terminology wiki
- [l10n-tw Glossaries](https://hackmd.io/@l10n-tw/glossaries) - Taiwan localization glossaries
- [兩岸術語對照表](https://zh.wikibooks.org/zh/%E5%A4%A7%E9%99%86%E5%8F%B0%E6%B9%BE%E8%AE%A1%E7%AE%97%E6%9C%BA%E6%9C%AF%E8%AF%AD%E5%AF%B9%E7%85%A7%E8%A1%A8) - Cross-strait terminology comparison
