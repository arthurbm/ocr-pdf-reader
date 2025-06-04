#!/usr/bin/env python3
"""
Specific test for the functionality of removing the last non-alphabetic character.
"""

import sys
import os

# Add src directory to path to import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from ocr_pdf_reader.text_processor import process_text_lines


def test_remove_ending_in_real_context():
    """
    Tests removal of last character in real context with codes.
    """
    # Simulate OCR extracted text with non-alphabetic characters at the end
    problematic_text = """
11.01.39 - INSTITUTE OF AFRICAN STUDIES - GR]
11.01.42 - ADMINISTRATIVE COORDINATION - GR1
11.01.55 - PROCESS ANALYSIS DIVISION - GR.
11.01.56 - PROTOCOL DIVISION - CCsA)
11.01.84 - PROGRAM SECRETARIAT - PROGEPE2
"""
    
    print("ORIGINAL TEXT (with problematic characters at the end):")
    print("=" * 60)
    for line in problematic_text.strip().split('\n'):
        if line.strip():
            print(f"'{line.strip()}'")
    
    # Process the text
    result = process_text_lines(problematic_text)
    
    print("\nPROCESSED TEXT (problematic characters removed):")
    print("=" * 60)
    for i, line in enumerate(result, 1):
        print(f"{i:2d}: '{line}'")
    
    # Verifications
    expected_endings = ['GR', 'GR', 'GR', 'CCsA', 'PROGEPE']
    
    print("\nVERIFICATIONS:")
    print("-" * 30)
    
    for i, line in enumerate(result):
        if i < len(expected_endings):
            expected_end = expected_endings[i]
            if line.endswith(expected_end):
                print(f"✅ Line {i+1}: Correctly ends with '{expected_end}'")
            else:
                print(f"❌ Line {i+1}: Should end with '{expected_end}', but ends with '{line[-10:]}'")
        
        # Check if last character is a letter
        if line and line[-1].isalpha():
            print(f"✅ Line {i+1}: Last character '{line[-1]}' is a letter")
        else:
            print(f"❌ Line {i+1}: Last character '{line[-1] if line else 'N/A'}' is not a letter")
    
    return result


if __name__ == "__main__":
    print("=== TEST: Removal of Non-Alphabetic Characters at End ===\n")
    test_remove_ending_in_real_context()
    print("\n=== END OF TEST ===") 