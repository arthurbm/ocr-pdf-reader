"""
Centralized configurations for the OCR PDF Reader.
"""

from pathlib import Path

# Project version
VERSION = "1.0.0"

# OCR configurations
OCR_CONFIG = {
    'default_language': 'eng',
    'custom_config': r'--oem 3 --psm 6',
    'supported_languages': ['eng', 'por', 'spa', 'fra', 'deu'],
}

# Image processing configurations
IMAGE_CONFIG = {
    'resolution_multiplier': 2.0,  # For page rendering
    'kernel_size': (1, 1),         # For morphology
    'threshold_method': 'OTSU',
}

# Text processing configurations
TEXT_CONFIG = {
    'min_line_length': 3,
    'remove_duplicates': True,
    'validate_lines': True,
}

# Regex patterns for different formats
REGEX_PATTERNS = {
    'standard': r'(\d+(?:[\.\,]\d+)*(?:[\.\,]\d+)*)\s*-\s*([^0-9]+?)(?=\s+\d+(?:[\.\,]\d+)*\s*-|\s*$)',
    'simple': r'(\d+)\s*-\s*(.+?)(?=\s+\d+\s*-|\s*$)',
    'complex': r'(\d+[\.\,\-]+[\d\.\,\-]*)\s*-\s*(.+?)(?=\s+\d+[\.\,\-]+[\d\.\,\-]*\s*-|\s*$)',
}

# Output configurations
OUTPUT_CONFIG = {
    'default_filename': 'extracted_text.txt',
    'encoding': 'utf-8',
    'show_progress': True,
    'max_preview_lines': 10,
}

# Path configurations
PATHS = {
    'temp_dir': Path.cwd() / 'temp',
    'output_dir': Path.cwd(),
    'logs_dir': Path.cwd() / 'logs',
}

# Create directories if they don't exist
for path in PATHS.values():
    path.mkdir(exist_ok=True)

# Logging configurations
LOGGING_CONFIG = {
    'level': 'INFO',
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'filename': PATHS['logs_dir'] / 'ocr_pdf_reader.log'
} 