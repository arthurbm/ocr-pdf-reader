"""
Interface de linha de comando para o OCR PDF Reader.
"""

import argparse
import sys
from pathlib import Path
from .core import extract_and_save
from .image_processor import check_tesseract_installation


def show_installation_help():
    """Mostra instruções de instalação do Tesseract."""
    print("AVISO: Tesseract OCR não encontrado!")
    print("Para instalar:")
    print("  Ubuntu/Debian: sudo apt install tesseract-ocr tesseract-ocr-por")
    print("  Windows: baixe de https://github.com/UB-Mannheim/tesseract/wiki")
    print("  macOS: brew install tesseract")


def main():
    """Função principal da CLI."""
    parser = argparse.ArgumentParser(
        description="Extrai texto de PDFs com imagens usando OCR",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos de uso:
  ocr-pdf-reader arquivo.pdf                      # Extrai texto para texto_extraido.txt
  ocr-pdf-reader arquivo.pdf -o resultado.txt     # Especifica arquivo de saída
  ocr-pdf-reader arquivo.pdf --lang eng           # Usa inglês para OCR
  ocr-pdf-reader arquivo.pdf --no-validate        # Não valida linhas extraídas
        """
    )
    
    parser.add_argument(
        'pdf_path',
        help='Caminho para o arquivo PDF'
    )
    
    parser.add_argument(
        '-o', '--output',
        default='texto_extraido.txt',
        help='Arquivo de saída (padrão: texto_extraido.txt)'
    )
    
    parser.add_argument(
        '--lang',
        default='por',
        help='Idioma para OCR (padrão: por)'
    )
    
    parser.add_argument(
        '--no-validate',
        action='store_true',
        help='Não valida as linhas extraídas'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='OCR PDF Reader 1.0.0'
    )
    
    args = parser.parse_args()
    
    # Verifica se o Tesseract está instalado
    if not check_tesseract_installation():
        show_installation_help()
        return 1
    
    # Verifica se o arquivo existe
    pdf_path = Path(args.pdf_path)
    if not pdf_path.exists():
        print(f"Erro: Arquivo não encontrado: {args.pdf_path}")
        return 1
    
    try:
        print(f"OCR PDF Reader v1.0.0")
        print(f"Arquivo: {args.pdf_path}")
        print(f"Idioma: {args.lang}")
        print(f"Saída: {args.output}")
        print("-" * 50)
        
        # Extrai o texto
        text_lines = extract_and_save(
            pdf_path=str(pdf_path),
            output_file=args.output,
            lang=args.lang,
            validate=not args.no_validate
        )
        
        if text_lines:
            print(f"\n✅ Sucesso! {len(text_lines)} linhas extraídas.")
            print(f"Resultado salvo em: {args.output}")
            return 0
        else:
            print("\n❌ Nenhum texto foi extraído.")
            return 1
            
    except FileNotFoundError as e:
        print(f"Erro: {e}")
        return 1
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return 1


def interactive_mode():
    """Modo interativo para usar sem parâmetros de linha de comando."""
    print("=== OCR PDF Reader - Modo Interativo ===")
    
    # Verifica Tesseract
    if not check_tesseract_installation():
        show_installation_help()
        return
    
    # Solicita caminho do PDF
    pdf_path = input("Digite o caminho para o arquivo PDF: ").strip()
    
    if not pdf_path:
        print("Erro: É necessário fornecer o caminho para um arquivo PDF.")
        return
    
    try:
        # Extrai o texto
        text_lines = extract_and_save(pdf_path)
        
        if text_lines:
            print(f"\n{'='*50}")
            print(f"TEXTO EXTRAÍDO ({len(text_lines)} linhas):")
            print(f"{'='*50}")
            
            # Mostra primeiras 10 linhas
            for i, line in enumerate(text_lines[:10], 1):
                print(f"{i:3d}: {line}")
            
            if len(text_lines) > 10:
                print(f"... e mais {len(text_lines) - 10} linhas")
            
            print(f"\nTexto completo salvo em: texto_extraido.txt")
        else:
            print("Nenhum texto foi extraído do PDF.")
            
    except Exception as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        interactive_mode()
    else:
        sys.exit(main()) 