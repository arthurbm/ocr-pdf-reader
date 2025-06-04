"""
OCR PDF Reader - Extração de texto de PDFs com imagens usando OCR

Este pacote oferece funcionalidades para extrair texto de arquivos PDF que contêm imagens,
aplicando técnicas de OCR (Optical Character Recognition) e processamento de texto.
"""

__version__ = "1.0.0"
__author__ = "Arthur"
__description__ = "Extração de texto de PDFs com imagens usando OCR"

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