# Python Documentation Translation Dictionary

This document describes the terminology dictionaries for maintaining translation consistency across the Python documentation project.

## Overview

The translation dictionary project provides curated key terms and their translations to help translators maintain consistent terminology usage across different documents. The dictionaries are maintained using LLM knowledge to identify and categorize important Python terminology.

## Generated Files

### terminology_dictionary.csv
The complete terminology dictionary containing important terms identified from Python documentation. Contains:
- **source_term**: The original English term
- **translated_term**: The corresponding Chinese (Traditional) translation  
- **frequency**: Number of occurrences across all files
- **files_count**: Number of different files containing this term
- **source_file**: Example file where this term was found
- **directory**: Directory of the source file
- **example_files**: List of up to 5 files containing this term

Total entries: ~14,700 unique terms

### focused_terminology_dictionary.csv
A curated subset of ~2,900 terms focusing on the most important Python terminology. Includes additional columns:
- **priority**: High/Medium priority classification
- **category**: Term classification

#### Categories:
- **Core Concepts** (7 terms): class, function, method, module, package, object, type
- **Built-in Types** (9 terms): int, str, list, dict, tuple, set, float, bool, complex  
- **Keywords/Constants** (8 terms): None, True, False, return, import, def, async, await
- **Exceptions** (690 terms): All *Error and *Exception terms
- **Code Elements** (825 terms): Terms in backticks, magic methods
- **Common Terms** (1,365 terms): Frequently used technical terms

## Maintenance

The terminology dictionaries are maintained using LLM knowledge to identify important Python terms and their translations. The dictionaries can be updated as needed to reflect new terminology or improved translations.

## Integration with Translation Workflow

### For New Translators
1. Start with `focused_terminology_dictionary.csv`
2. Learn standard translations for core Python concepts
3. Reference high-frequency terms for consistency

### For Translation Review
1. Check new translations against the dictionary
2. Verify consistent terminology usage
3. Update dictionary when establishing new standard translations

### For Project Management
1. Track translation progress for key technical terms
2. Identify terminology needing standardization
3. Prioritize translation efforts using frequency data

### Output Format
CSV files use UTF-8 encoding to properly handle Chinese characters. Compatible with Excel, Google Sheets, and other spreadsheet applications.

## Maintenance

### Adding New Patterns
To extend pattern recognition, modify `extract_key_terms()` function in `extract_terminology.py`:

```python
# Add new technical patterns
tech_patterns = [
    r'\b(?:new_pattern_here)\b',
    # existing patterns...
]
```

### Adjusting Filters
Modify filtering criteria in `is_significant_term()` and `create_focused_dictionary()` functions.

### Performance Optimization
- Current processing: ~509 files in 2-3 minutes
- Memory usage: ~50MB peak
- Scalable to larger repositories

This documentation provides comprehensive guidance for maintaining and using the translation dictionary system to ensure consistent, high-quality Python documentation translation.