#!/usr/bin/env python3
"""
Test of broken line processing functionality
"""

import sys
import os

# Add src directory to path to import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from ocr_pdf_reader.text_processor import process_text_lines


def test_line_breaking():
    """
    Tests broken line processing.
    """
    # Simulate OCR extracted text with broken lines
    ocr_text = """
1 - This is the first item which can have
a very long line that was broken
by OCR into multiple lines
2 - This is the second item which can also
be broken into several lines
as extracted by OCR
3 - Third short item
4 - Fourth item which again has a
very long line that can be broken
when OCR processes the image
5 - Fifth and last item
"""
    
    print("ORIGINAL TEXT (simulating OCR):")
    print("=" * 50)
    print(ocr_text)
    
    # Process the text
    processed_lines = process_text_lines(ocr_text)
    
    print("\nPROCESSED TEXT:")
    print("=" * 50)
    for i, line in enumerate(processed_lines, 1):
        print(f"{i}: {line}")
    
    return processed_lines


def test_edge_cases():
    """
    Tests special formatting cases.
    """
    print("\n" + "=" * 60)
    print("TESTING SPECIAL CASES")
    print("=" * 60)
    
    # Test 1: Numbers without dash
    text1 = """
1 First item without dash
continuation of first line
2 Second item without dash
"""
    print("\nTest 1 - Numbers without dash:")
    print("Input:", repr(text1))
    result1 = process_text_lines(text1)
    print("Result:", result1)
    
    # Test 2: Mixed formatting
    text2 = """
1. - Item with dot and dash
continuation of this line
2) Item with parentheses
but without dash
3 - Normal item with dash
and its continuation
"""
    print("\nTest 2 - Mixed formatting:")
    print("Input:", repr(text2))
    result2 = process_text_lines(text2)
    print("Result:", result2)
    
    # Test 3: Blank lines and spaces
    text3 = """
1 - First item

continuation after blank line

2 - Second item
   with extra spaces
      and indentation
3 - Third item
"""
    print("\nTest 3 - Blank lines and spaces:")
    print("Input:", repr(text3))
    result3 = process_text_lines(text3)
    print("Result:", result3)


if __name__ == "__main__":
    # Run tests
    print("🧪 TESTING BROKEN LINE PROCESSING")
    print("=" * 60)
    
    lines = test_line_breaking()
    test_edge_cases()
    
    print(f"\n✅ Test completed! Total processed lines: {len(lines)}") 