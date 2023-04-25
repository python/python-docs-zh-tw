# Scripts

Useful scripts for the translation.

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
