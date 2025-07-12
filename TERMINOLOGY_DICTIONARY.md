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

Total entries: ~196 essential Python terms

### focused_terminology_dictionary.csv
A curated subset of ~118 terms focusing on the most important Python terminology. Includes additional columns:
- **priority**: High/Medium priority classification
- **category**: Term classification

#### Categories:
- **Core Concepts** (7 terms): class, function, method, module, package, object, type
- **Built-in Types** (9 terms): int, str, list, dict, tuple, set, float, bool, complex  
- **Keywords/Constants** (25 terms): None, True, False, return, import, def, async, await, and other Python keywords
- **Exceptions** (29 terms): Common *Error and *Exception classes
- **Code Elements** (14 terms): Magic methods like __init__, __str__, etc.
- **Common Terms** (34 terms): Important technical concepts like decorator, generator, iterator

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

### Adding New Terms
New terms can be identified and added based on:
- Frequency of appearance in documentation
- Importance to Python concepts
- Consistency needs across translation files

### Manual Curation Process
The dictionaries are maintained through careful analysis of:
- Core Python terminology in official documentation
- Existing translation patterns in .po files
- Category-based organization for translator efficiency

### Quality Assurance
- Regular review of term translations for consistency
- Cross-reference with official Python terminology
- Validation against established translation conventions

This documentation provides comprehensive guidance for maintaining and using the translation dictionary system to ensure consistent, high-quality Python documentation translation.