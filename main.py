#!/usr/bin/env python3
"""
Main compatibility script for the OCR PDF Reader.

This script maintains compatibility with the previous version,
but now uses the new modular architecture.
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from ocr_pdf_reader import extract_text_from_pdf
from ocr_pdf_reader.image_processor import check_tesseract_installation


def main():
    """
    Main function of the script - compatibility with previous version.
    """
    # Check if tesseract is installed
    if not check_tesseract_installation():
        print("WARNING: Tesseract OCR not found!")
        print("To install on Ubuntu/Debian: sudo apt install tesseract-ocr tesseract-ocr-eng")
        print("To install on Windows: download from https://github.com/UB-Mannheim/tesseract/wiki")
        print("To install on macOS: brew install tesseract")
        return []
    else:
        print("Tesseract OCR found!")
    
    # Example usage
    pdf_path = input("Enter the path to the PDF file: ").strip()
    
    if not pdf_path:
        print("Error: You must provide the path to a PDF file.")
        return []
    
    try:
        # Extract text using the new architecture
        text_lines = extract_text_from_pdf(pdf_path)
        
        if text_lines:
            print(f"\n{'='*50}")
            print(f"EXTRACTED TEXT ({len(text_lines)} lines):")
            print(f"{'='*50}")
            
            for i, line in enumerate(text_lines, 1):
                print(f"{i:3d}: {line}")
            
            # Save to text file
            output_file = "extracted_text.txt"
            with open(output_file, 'w', encoding='utf-8') as f:
                for line in text_lines:
                    f.write(line + '\n')
            
            print(f"\nText saved to: {output_file}")
            
            # Return the array as requested
            return text_lines
        else:
            print("No text was extracted from the PDF.")
            return []
            
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []


if __name__ == "__main__":
    main()
