"""
Main entry point for the OCR PDF Reader.

Allows running the module with: python -m ocr_pdf_reader
"""

from .cli import main, interactive_mode
import sys


if __name__ == "__main__":
    if len(sys.argv) == 1:
        # Interactive mode when no arguments are provided
        interactive_mode()
    else:
        # CLI mode with arguments
        sys.exit(main()) 