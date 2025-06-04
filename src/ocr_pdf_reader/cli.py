"""
Command line interface for the OCR PDF Reader.
"""

import argparse
import sys
from pathlib import Path
from .core import extract_and_save
from .image_processor import check_tesseract_installation


def show_installation_help():
    """Shows Tesseract installation instructions."""
    print("WARNING: Tesseract OCR not found!")
    print("To install:")
    print("  Ubuntu/Debian: sudo apt install tesseract-ocr tesseract-ocr-eng")
    print("  Windows: download from https://github.com/UB-Mannheim/tesseract/wiki")
    print("  macOS: brew install tesseract")


def main():
    """Main CLI function."""
    parser = argparse.ArgumentParser(
        description="Extract text from PDFs with images using OCR",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Usage examples:
  ocr-pdf-reader file.pdf                         # Extract text to extracted_text.txt
  ocr-pdf-reader file.pdf -o result.txt           # Specify output file
  ocr-pdf-reader file.pdf --lang eng              # Use English for OCR
  ocr-pdf-reader file.pdf --no-validate           # Don't validate extracted lines
        """
    )
    
    parser.add_argument(
        'pdf_path',
        help='Path to the PDF file'
    )
    
    parser.add_argument(
        '-o', '--output',
        default='extracted_text.txt',
        help='Output file (default: extracted_text.txt)'
    )
    
    parser.add_argument(
        '--lang',
        default='eng',
        help='Language for OCR (default: eng)'
    )
    
    parser.add_argument(
        '--no-validate',
        action='store_true',
        help='Don\'t validate extracted lines'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='OCR PDF Reader 1.0.0'
    )
    
    args = parser.parse_args()
    
    # Check if Tesseract is installed
    if not check_tesseract_installation():
        show_installation_help()
        return 1
    
    # Check if file exists
    pdf_path = Path(args.pdf_path)
    if not pdf_path.exists():
        print(f"Error: File not found: {args.pdf_path}")
        return 1
    
    try:
        print(f"OCR PDF Reader v1.0.0")
        print(f"File: {args.pdf_path}")
        print(f"Language: {args.lang}")
        print(f"Output: {args.output}")
        print("-" * 50)
        
        # Extract text
        text_lines = extract_and_save(
            pdf_path=str(pdf_path),
            output_file=args.output,
            lang=args.lang,
            validate=not args.no_validate
        )
        
        if text_lines:
            print(f"\n✅ Success! {len(text_lines)} lines extracted.")
            print(f"Result saved to: {args.output}")
            return 0
        else:
            print("\n❌ No text was extracted.")
            return 1
            
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}")
        return 1


def interactive_mode():
    """Interactive mode for use without command line parameters."""
    print("=== OCR PDF Reader - Interactive Mode ===")
    
    # Check Tesseract
    if not check_tesseract_installation():
        show_installation_help()
        return
    
    # Request PDF path
    pdf_path = input("Enter the path to the PDF file: ").strip()
    
    if not pdf_path:
        print("Error: You must provide the path to a PDF file.")
        return
    
    try:
        # Extract text
        text_lines = extract_and_save(pdf_path)
        
        if text_lines:
            print(f"\n{'='*50}")
            print(f"EXTRACTED TEXT ({len(text_lines)} lines):")
            print(f"{'='*50}")
            
            # Show first 10 lines
            for i, line in enumerate(text_lines[:10], 1):
                print(f"{i:3d}: {line}")
            
            if len(text_lines) > 10:
                print(f"... and {len(text_lines) - 10} more lines")
            
            print(f"\nComplete text saved to: extracted_text.txt")
        else:
            print("No text was extracted from the PDF.")
            
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        interactive_mode()
    else:
        sys.exit(main()) 