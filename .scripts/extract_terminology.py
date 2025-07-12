#!/usr/bin/env python3
"""
Extract terminology from .po files and build a translation dictionary.

This script processes all .po files in the repository to extract key terms
and their translations, focusing on terminology rather than full sentences.
The output is a CSV file that can serve as a reference for translators.
"""

import csv
import glob
import re
import polib
from pathlib import Path
from collections import defaultdict, Counter


def is_significant_term(msgid: str, msgstr: str) -> bool:
    """
    Determine if a msgid/msgstr pair represents significant terminology.
    
    Filters out:
    - Empty strings
    - Very long texts (likely full sentences)
    - Pure punctuation or symbols
    - Common English words
    - Single characters
    """
    if not msgid.strip() or not msgstr.strip():
        return False
    
    # Skip very long texts (likely full sentences/paragraphs)
    if len(msgid) > 80:
        return False
    
    # Skip single characters unless they're meaningful symbols
    if len(msgid.strip()) == 1:
        return False
    
    # Skip pure punctuation
    if re.match(r'^[^\w\s]+$', msgid.strip()):
        return False
    
    # Skip strings that are just whitespace or formatting
    if re.match(r'^\s*$', msgid.strip()):
        return False
    
    # Skip common English words that aren't technical terms
    common_words = {
        'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by',
        'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did',
        'will', 'would', 'could', 'should', 'may', 'might', 'can', 'must', 'shall',
        'this', 'that', 'these', 'those', 'here', 'there', 'where', 'when', 'why', 'how',
        'if', 'then', 'else', 'while', 'until', 'before', 'after', 'during', 'since',
        'not', 'no', 'yes', 'all', 'any', 'some', 'many', 'much', 'more', 'most', 'less', 'least',
        'one', 'two', 'three', 'first', 'second', 'third', 'last', 'next', 'previous',
        'as', 'so', 'too', 'very', 'just', 'only', 'also', 'even', 'still', 'yet'
    }
    
    # Skip if the entire msgid is just common words
    words = re.findall(r'\b\w+\b', msgid.lower())
    if len(words) <= 3 and all(word in common_words for word in words):
        return False
    
    return True


def extract_key_terms(msgid: str) -> list:
    """
    Extract key terms from a msgid string.
    
    This function identifies:
    - Technical terms in backticks
    - Class/function names with parentheses
    - Standalone technical words
    - Terms with specific patterns
    """
    terms = []
    
    # Extract terms in backticks (code terms) - these are high priority
    backtick_terms = re.findall(r'`([^`]+)`', msgid)
    for term in backtick_terms:
        # Clean up the term
        clean_term = re.sub(r'[^\w\s\.\(\)_-]', '', term).strip()
        if clean_term and len(clean_term) > 1:
            terms.append(clean_term)
    
    # Extract terms that look like class/function names
    code_terms = re.findall(r'\b[A-Z][a-zA-Z0-9_]*(?:\(\))?|\b[a-z_][a-z0-9_]*\(\)', msgid)
    terms.extend([term for term in code_terms if len(term) > 2])
    
    # For short strings (likely terminology), include the whole string if it looks technical
    if len(msgid.strip()) <= 40 and not any(char in msgid for char in '.!?;'):
        # Check if it contains technical indicators
        if any(indicator in msgid.lower() for indicator in [
            'python', 'class', 'function', 'method', 'module', 'package', 'library',
            'api', 'http', 'url', 'json', 'xml', 'sql', 'html', 'css', 'error',
            'exception', 'object', 'type', 'int', 'str', 'list', 'dict', 'tuple',
            'file', 'directory', 'path', 'import', 'return', 'yield', 'async',
            'await', 'def', 'lambda', 'self', 'cls'
        ]):
            terms.append(msgid.strip())
    
    # Extract specific technical terms patterns
    tech_patterns = [
        r'\b(?:class|function|method|module|package|library|framework|API|HTTP|URL|JSON|XML|SQL|HTML|CSS|JavaScript|Python)\b',
        r'\b[a-z]+(?:[A-Z][a-z]*)+\b',  # camelCase terms
        r'\b[A-Z][a-z]*(?:[A-Z][a-z]*)*\b',  # PascalCase terms
        r'\b\w*Error\b',  # Error types
        r'\b\w*Exception\b',  # Exception types
        r'\b__\w+__\b',  # Magic methods/attributes
    ]
    
    for pattern in tech_patterns:
        matches = re.findall(pattern, msgid, re.IGNORECASE)
        terms.extend([match for match in matches if len(match) > 2])
    
    # Remove duplicates while preserving order
    seen = set()
    unique_terms = []
    for term in terms:
        term_clean = term.strip()
        if term_clean and term_clean not in seen and len(term_clean) > 1:
            seen.add(term_clean)
            unique_terms.append(term_clean)
    
    return unique_terms


def process_po_file(filepath: str) -> list:
    """
    Process a single .po file and extract terminology pairs.
    
    Returns a list of tuples: (msgid, msgstr, file_path)
    """
    try:
        po = polib.pofile(filepath)
        terms = []
        
        for entry in po:
            if not entry.msgid or not entry.msgstr:
                continue
                
            # Skip untranslated entries
            if not entry.translated():
                continue
            
            # Process based on different criteria
            msgid_clean = entry.msgid.strip()
            msgstr_clean = entry.msgstr.strip()
            
            # High priority: Terms in backticks (code elements)
            backtick_terms = re.findall(r'`([^`]+)`', entry.msgid)
            for term in backtick_terms:
                clean_term = re.sub(r'[^\w\s\.\(\)_-]', '', term).strip()
                if clean_term and len(clean_term) > 1:
                    terms.append((clean_term, msgstr_clean, filepath))
            
            # Medium priority: Short technical terms
            if is_significant_term(msgid_clean, msgstr_clean):
                # For short terms that look technical, use the whole msgid
                if len(msgid_clean) <= 40 and any(indicator in msgid_clean.lower() for indicator in [
                    'python', 'class', 'function', 'method', 'module', 'package', 'error',
                    'exception', 'object', 'type', 'import', 'return', 'def', 'api'
                ]):
                    terms.append((msgid_clean, msgstr_clean, filepath))
                
                # Extract key technical terms from longer strings
                key_terms = extract_key_terms(entry.msgid)
                for term in key_terms:
                    if len(term) > 2:  # Skip very short terms
                        terms.append((term, msgstr_clean, filepath))
        
        return terms
        
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return []


def main():
    """Main function to extract terminology and generate CSV."""
    
    # Find all .po files in the repository
    base_dir = Path(".")
    po_files = glob.glob(str(base_dir / "**/*.po"), recursive=True)
    
    print(f"Found {len(po_files)} .po files")
    
    # Collect all terminology
    all_terms = []
    term_frequency = Counter()
    term_files = defaultdict(set)
    
    for po_file in po_files:
        print(f"Processing {po_file}...")
        terms = process_po_file(po_file)
        
        for msgid, msgstr, filepath in terms:
            # Normalize the term for frequency counting
            term_key = msgid.lower().strip()
            term_frequency[term_key] += 1
            term_files[term_key].add(Path(filepath).name)
            
            all_terms.append({
                'source_term': msgid,
                'translated_term': msgstr,
                'source_file': Path(filepath).name,
                'directory': Path(filepath).parent.name
            })
    
    # Sort terms by frequency (most common first)
    print(f"Extracted {len(all_terms)} term instances")
    print(f"Found {len(term_frequency)} unique terms")
    
    # Create CSV output
    output_file = "terminology_dictionary.csv"
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['source_term', 'translated_term', 'frequency', 'files_count', 
                     'source_file', 'directory', 'example_files']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
        # Process unique terms with their frequency information
        # Sort by frequency (most common first) and filter for meaningful terms
        processed_terms = set()
        sorted_terms = sorted(term_frequency.items(), key=lambda x: x[1], reverse=True)
        
        for term_key, frequency in sorted_terms:
            # Skip terms that appear only once unless they're clearly technical
            if frequency == 1 and not any(indicator in term_key for indicator in [
                'python', 'class', 'function', 'method', 'error', 'exception', 'api', 
                'http', 'json', 'xml', 'sql', 'import', '__', '()', 'async', 'await'
            ]):
                continue
            
            # Find an example term data for this term_key
            example_term_data = None
            for term_data in all_terms:
                if term_data['source_term'].lower().strip() == term_key:
                    example_term_data = term_data
                    break
            
            if not example_term_data:
                continue
            
            processed_terms.add(term_key)
            
            writer.writerow({
                'source_term': example_term_data['source_term'],
                'translated_term': example_term_data['translated_term'],
                'frequency': frequency,
                'files_count': len(term_files[term_key]),
                'source_file': example_term_data['source_file'],
                'directory': example_term_data['directory'],
                'example_files': '; '.join(list(term_files[term_key])[:5])  # First 5 files
            })
    
    print(f"Terminology dictionary saved to {output_file}")
    
    # Print some statistics
    print(f"\nStatistics:")
    print(f"Total unique terms: {len(processed_terms)}")
    print(f"Most common terms:")
    for term, count in term_frequency.most_common(10):
        print(f"  {term}: {count} occurrences")


if __name__ == "__main__":
    main()