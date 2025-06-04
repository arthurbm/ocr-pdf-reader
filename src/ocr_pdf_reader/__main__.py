"""
Ponto de entrada principal para o OCR PDF Reader.

Permite executar o módulo com: python -m ocr_pdf_reader
"""

from .cli import main, interactive_mode
import sys


if __name__ == "__main__":
    if len(sys.argv) == 1:
        # Modo interativo quando não há argumentos
        interactive_mode()
    else:
        # Modo CLI com argumentos
        sys.exit(main()) 