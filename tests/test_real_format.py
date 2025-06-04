#!/usr/bin/env python3
"""
Test with real PDF format from user
"""

import sys
import os

# Add src directory to path to import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from ocr_pdf_reader.text_processor import process_text_lines


def test_real_format():
    """
    Tests processing with real PDF format.
    """
    # Simulate part of the real text extracted from PDF
    real_text = """11.01.39 - INSTITUTE OF AFRICAN STUDIES - GR 11.01.42 - ADMINISTRATIVE COORDINATION - GR 11.01.55 - PROCESS ANALYSIS DIVISION - GR 11.01.56 - PROTOCOL DIVISION - GR 11.01.84 - CONTRACT AND AGREEMENT ANALYSIS AND MONITORING DIVISION - GR 11.01,44 - INFORMATION TECHNOLOGY SUPPORT DIVISION - GR 11.01.45 - COMPUTER WORKSHOP - GR 11.01.46 - RECTORY TRANSPORTATION SERVICE 11.01.48 - SECRETARIAT OF OPEN AND DIGITAL EDUCATION PROGRAMS - GR"""
    
    print("ORIGINAL TEXT (real format):")
    print("=" * 60)
    print(real_text[:200] + "...")
    
    # Process the text
    processed_lines = process_text_lines(real_text)
    
    print(f"\nPROCESSED TEXT ({len(processed_lines)} lines):")
    print("=" * 60)
    for i, line in enumerate(processed_lines[:10], 1):  # Show only first 10
        print(f"{i:2d}: {line}")
    
    if len(processed_lines) > 10:
        print(f"... and {len(processed_lines) - 10} more lines")
    
    return processed_lines


def test_with_actual_file():
    """
    Tests with real extracted file.
    """
    print("\n" + "=" * 60)
    print("TESTING WITH REAL FILE")
    print("=" * 60)
    
    try:
        with open('extracted_text.txt', 'r', encoding='utf-8') as f:
            complete_text = f.read()
        
        # Process the text
        processed_lines = process_text_lines(complete_text)
        
        print(f"Total processed lines: {len(processed_lines)}")
        print("\nFirst 10 processed lines:")
        print("-" * 40)
        
        for i, line in enumerate(processed_lines[:10], 1):
            print(f"{i:2d}: {line}")
        
        if len(processed_lines) > 10:
            print(f"\n... and {len(processed_lines) - 10} more lines")
        
        # Save the processed result
        with open('corrected_result.txt', 'w', encoding='utf-8') as f:
            for line in processed_lines:
                f.write(line + '\n')
        
        print(f"\n✅ Result saved to 'corrected_result.txt'")
        return processed_lines
        
    except FileNotFoundError:
        print("❌ File 'extracted_text.txt' not found!")
        return []


if __name__ == "__main__":
    print("🧪 TESTING PROCESSING WITH REAL FORMAT")
    print("=" * 60)
    
    # Test with sample
    sample_lines = test_real_format()
    
    # Test with complete file
    complete_lines = test_with_actual_file()
    
    print(f"\n✅ Test completed!")
    print(f"Sample: {len(sample_lines)} lines")
    print(f"Complete file: {len(complete_lines)} lines") 