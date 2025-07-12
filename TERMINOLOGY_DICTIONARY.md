# Python Documentation Translation Dictionary

This document describes the terminology extraction tools and outputs for maintaining translation consistency across the Python documentation project.

## Overview

The translation dictionary project extracts key terms and their translations from all .po files in the repository to help translators maintain consistent terminology usage across different documents.

## Generated Files

### terminology_dictionary.csv
The complete terminology dictionary extracted from all 509 .po files. Contains:
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

## Tools

### extract_terminology.py

Main extraction script with intelligent filtering:

**Features:**
- Processes all .po files recursively
- Filters out common English words (the, and, for, etc.)
- Prioritizes technical terminology
- Extracts code elements from backticks
- Identifies Python-specific patterns
- Tracks frequency and file distribution

**Algorithm:**
1. Scans all .po files for msgid/msgstr pairs
2. Applies significance filters (length, technical content, frequency)
3. Extracts key terms using pattern matching
4. Aggregates frequency and file location data
5. Sorts by frequency and generates CSV output

**Usage:**
```bash
cd /path/to/python-docs-zh-tw
python3 .scripts/extract_terminology.py
```

**Runtime:** ~2-3 minutes for 509 files

### create_focused_dictionary.py

Post-processing script for curation:

**Features:**
- Filters for high-priority terms
- Categorizes by term type
- Assigns priority levels
- Creates translator-friendly output

**Criteria for inclusion:**
- Python built-in types and keywords (high priority)
- Terms appearing in 20+ files with 10+ frequency  
- Code elements and exception types
- Technical patterns (Error, Exception, Class, etc.)

**Usage:**
```bash
cd /path/to/python-docs-zh-tw  
python3 .scripts/create_focused_dictionary.py
```

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

## Examples

### High-Priority Core Terms
```csv
source_term,translated_term,frequency,files_count,priority,category
class,abstract base class（抽象基底類別）,921,141,High,Core Concepts
function,呼叫函式時被傳遞給,315,116,High,Core Concepts
None,如果一個物件是不滅的,518,121,High,Keywords/Constants
```

### Exception Terms
```csv
source_term,translated_term,frequency,files_count,priority,category  
ValueError,若 list 中無此元素則會觸發,103,48,High,Exceptions
TypeError,錯誤訊息的最後一行指示發生了什麼事,49,29,High,Exceptions
```

## Regeneration Process

To update the dictionaries after new translations:

```bash
# Full extraction (2-3 minutes)
python3 .scripts/extract_terminology.py

# Create focused version (< 1 minute)  
python3 .scripts/create_focused_dictionary.py
```

## Technical Details

### Filtering Algorithm
The extraction uses multiple filters to identify significant terminology:

1. **Length filtering**: Skip very short (< 2 chars) and very long (> 80 chars) terms
2. **Common word filtering**: Exclude frequent English words using predefined lists
3. **Technical pattern matching**: Identify Python-specific patterns
4. **Frequency filtering**: Prioritize terms appearing multiple times
5. **Code element extraction**: Special handling for backtick-enclosed terms

### Pattern Recognition
- **Code elements**: `function()`, `class.method` 
- **Magic methods**: `__init__`, `__str__`
- **Exception types**: `*Error`, `*Exception`
- **Type names**: `int`, `str`, `list`
- **Keywords**: `def`, `class`, `import`

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