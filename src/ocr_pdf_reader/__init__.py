"""
OCR PDF Reader - Text extraction from PDFs with images using OCR

This package provides functionalities to extract text from PDF files containing images,
applying OCR (Optical Character Recognition) and text processing techniques.
"""

__version__ = "1.0.0"
__author__ = "Arthur"
__description__ = "Text extraction from PDFs with images using OCR"

from .core import extract_text_from_pdf
from .image_processor import extract_images_from_pdf, preprocess_image, extract_text_from_image
from .text_processor import process_text_lines

__all__ = [
    "extract_text_from_pdf",
    "extract_images_from_pdf", 
    "preprocess_image",
    "extract_text_from_image",
    "process_text_lines"
] 