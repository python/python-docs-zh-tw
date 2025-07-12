# Scripts

Useful scripts for the translation.

## Translation Dictionary Generation

Extract and build a translation dictionary for terminologies across different .po files to maintain consistency.

### extract_terminology.py
Main script that processes all .po files and extracts terminology:

```sh
python3 .scripts/extract_terminology.py
```

Generates `terminology_dictionary.csv` with all extracted terms and their translations.

### create_focused_dictionary.py
Creates a curated dictionary focusing on the most important Python terminology:

```sh
python3 .scripts/create_focused_dictionary.py
```

Generates `focused_terminology_dictionary.csv` with categorized high-priority terms.

See the terminology documentation for detailed usage and integration with translation workflow.

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
