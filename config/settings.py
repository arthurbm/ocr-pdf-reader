"""
Configurações centralizadas do OCR PDF Reader.
"""

from pathlib import Path

# Versão do projeto
VERSION = "1.0.0"

# Configurações do OCR
OCR_CONFIG = {
    'default_language': 'por',
    'custom_config': r'--oem 3 --psm 6',
    'supported_languages': ['por', 'eng', 'spa', 'fra', 'deu'],
}

# Configurações de processamento de imagem
IMAGE_CONFIG = {
    'resolution_multiplier': 2.0,  # Para renderização de páginas
    'kernel_size': (1, 1),         # Para morfologia
    'threshold_method': 'OTSU',
}

# Configurações de processamento de texto
TEXT_CONFIG = {
    'min_line_length': 3,
    'remove_duplicates': True,
    'validate_lines': True,
}

# Padrões de regex para diferentes formatos
REGEX_PATTERNS = {
    'standard': r'(\d+(?:[\.\,]\d+)*(?:[\.\,]\d+)*)\s*-\s*([^0-9]+?)(?=\s+\d+(?:[\.\,]\d+)*\s*-|\s*$)',
    'simple': r'(\d+)\s*-\s*(.+?)(?=\s+\d+\s*-|\s*$)',
    'complex': r'(\d+[\.\,\-]+[\d\.\,\-]*)\s*-\s*(.+?)(?=\s+\d+[\.\,\-]+[\d\.\,\-]*\s*-|\s*$)',
}

# Configurações de saída
OUTPUT_CONFIG = {
    'default_filename': 'texto_extraido.txt',
    'encoding': 'utf-8',
    'show_progress': True,
    'max_preview_lines': 10,
}

# Configurações de paths
PATHS = {
    'temp_dir': Path.cwd() / 'temp',
    'output_dir': Path.cwd(),
    'logs_dir': Path.cwd() / 'logs',
}

# Criar diretórios se não existirem
for path in PATHS.values():
    path.mkdir(exist_ok=True)

# Configurações de logging
LOGGING_CONFIG = {
    'level': 'INFO',
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'filename': PATHS['logs_dir'] / 'ocr_pdf_reader.log'
} 