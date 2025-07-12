#!/usr/bin/env python3
"""
Create a focused terminology dictionary for the most important Python terms.

This script extracts the most critical Python terminology for translation consistency.
"""

import csv
from collections import defaultdict, Counter


def create_focused_dictionary():
    """Create a focused dictionary with the most important terms."""
    
    # Read the full terminology dictionary
    important_terms = []
    
    with open("terminology_dictionary.csv", 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            source_term = row['source_term'].strip()
            frequency = int(row['frequency'])
            files_count = int(row['files_count'])
            
            # Focus on high-priority terms
            is_important = False
            
            # High priority: Python built-in types and keywords
            if source_term.lower() in {
                'class', 'function', 'method', 'module', 'package', 'object', 'type',
                'int', 'str', 'list', 'dict', 'tuple', 'set', 'float', 'bool', 'complex',
                'none', 'true', 'false', 'return', 'import', 'def', 'async', 'await',
                'lambda', 'yield', 'raise', 'try', 'except', 'finally', 'with', 'as'
            }:
                is_important = True
            
            # High priority: Common Python concepts
            elif any(concept in source_term.lower() for concept in [
                'exception', 'error', 'iterator', 'generator', 'decorator', 'property',
                'classmethod', 'staticmethod', 'metaclass', 'inheritance', 'polymorphism'
            ]):
                is_important = True
            
            # High priority: Terms that appear in many files (widespread usage)
            elif files_count >= 20 and frequency >= 10:
                is_important = True
            
            # Medium priority: Code elements in backticks
            elif '`' in source_term or source_term.startswith('__') and source_term.endswith('__'):
                is_important = True
            
            # Medium priority: Terms with technical patterns
            elif any(pattern in source_term for pattern in ['()', 'Error', 'Exception', 'Class']):
                is_important = True
            
            if is_important:
                important_terms.append(row)
    
    # Sort by frequency (most common first)
    important_terms.sort(key=lambda x: int(x['frequency']), reverse=True)
    
    # Write focused dictionary
    with open("focused_terminology_dictionary.csv", 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['source_term', 'translated_term', 'frequency', 'files_count', 
                     'priority', 'category', 'example_files']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
        for term_data in important_terms:
            source_term = term_data['source_term'].strip()
            
            # Categorize the term
            category = 'Other'
            priority = 'Medium'
            
            if source_term.lower() in {
                'class', 'function', 'method', 'module', 'package', 'object', 'type'
            }:
                category = 'Core Concepts'
                priority = 'High'
            elif source_term.lower() in {
                'int', 'str', 'list', 'dict', 'tuple', 'set', 'float', 'bool', 'complex'
            }:
                category = 'Built-in Types'
                priority = 'High'
            elif source_term.lower() in {
                'none', 'true', 'false', 'return', 'import', 'def', 'async', 'await'
            }:
                category = 'Keywords/Constants'
                priority = 'High'
            elif 'error' in source_term.lower() or 'exception' in source_term.lower():
                category = 'Exceptions'
                priority = 'High'
            elif '`' in source_term:
                category = 'Code Elements'
                priority = 'Medium'
            elif int(term_data['files_count']) >= 50:
                category = 'Common Terms'
                priority = 'High'
            
            writer.writerow({
                'source_term': source_term,
                'translated_term': term_data['translated_term'],
                'frequency': term_data['frequency'],
                'files_count': term_data['files_count'],
                'priority': priority,
                'category': category,
                'example_files': term_data['example_files']
            })
    
    print(f"Created focused terminology dictionary with {len(important_terms)} important terms")
    
    # Print category statistics
    categories = defaultdict(int)
    priorities = defaultdict(int)
    
    for term in important_terms:
        source_term = term['source_term'].strip()
        if source_term.lower() in {'class', 'function', 'method', 'module', 'package', 'object', 'type'}:
            categories['Core Concepts'] += 1
        elif source_term.lower() in {'int', 'str', 'list', 'dict', 'tuple', 'set', 'float', 'bool', 'complex'}:
            categories['Built-in Types'] += 1
        elif source_term.lower() in {'none', 'true', 'false', 'return', 'import', 'def', 'async', 'await'}:
            categories['Keywords/Constants'] += 1
        elif 'error' in source_term.lower() or 'exception' in source_term.lower():
            categories['Exceptions'] += 1
        elif '`' in source_term:
            categories['Code Elements'] += 1
        else:
            categories['Common Terms'] += 1
    
    print("\nCategory breakdown:")
    for category, count in categories.items():
        print(f"  {category}: {count} terms")


if __name__ == "__main__":
    create_focused_dictionary()