# Scripts

Useful scripts for the translation.

## Translation Dictionary

The repository includes terminology dictionaries (`terminology_dictionary.csv` and `focused_terminology_dictionary.csv`) that provide standard translations for important Python terms to maintain consistency across documents. These dictionaries are maintained using LLM knowledge and can be referenced by translators.

See `TERMINOLOGY_DICTIONARY.md` for detailed usage and integration with translation workflow.

## From Google Translation

Translate all untranslated entries of the given .po file with Google Translate.

```sh
.scripts/google_translate.sh library/csv.po
```

## From zh_CN Translation

If a specific doc has been translated into Simplified Chinese (zh_CN) and you'd like to adopt it as a base, you can insert the command:

```sh
.scripts/from_cn.sh library/csv.po
```
