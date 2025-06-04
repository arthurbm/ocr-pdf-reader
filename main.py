#!/usr/bin/env python3
"""
Script principal de compatibilidade para o OCR PDF Reader.

Este script mantém a compatibilidade com a versão anterior,
mas agora usa a nova arquitetura modular.
"""

import sys
import os

# Adiciona o diretório src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from ocr_pdf_reader import extract_text_from_pdf
from ocr_pdf_reader.image_processor import check_tesseract_installation


def main():
    """
    Função principal do script - compatibilidade com versão anterior.
    """
    # Verifica se o tesseract está instalado
    if not check_tesseract_installation():
        print("AVISO: Tesseract OCR não encontrado!")
        print("Para instalar no Ubuntu/Debian: sudo apt install tesseract-ocr tesseract-ocr-por")
        print("Para instalar no Windows: baixe de https://github.com/UB-Mannheim/tesseract/wiki")
        print("Para instalar no macOS: brew install tesseract")
        return []
    else:
        print("Tesseract OCR encontrado!")
    
    # Exemplo de uso
    pdf_path = input("Digite o caminho para o arquivo PDF: ").strip()
    
    if not pdf_path:
        print("Erro: É necessário fornecer o caminho para um arquivo PDF.")
        return []
    
    try:
        # Extrai o texto usando a nova arquitetura
        text_lines = extract_text_from_pdf(pdf_path)
        
        if text_lines:
            print(f"\n{'='*50}")
            print(f"TEXTO EXTRAÍDO ({len(text_lines)} linhas):")
            print(f"{'='*50}")
            
            for i, line in enumerate(text_lines, 1):
                print(f"{i:3d}: {line}")
            
            # Salva em arquivo de texto
            output_file = "texto_extraido.txt"
            with open(output_file, 'w', encoding='utf-8') as f:
                for line in text_lines:
                    f.write(line + '\n')
            
            print(f"\nTexto salvo em: {output_file}")
            
            # Retorna o array conforme solicitado
            return text_lines
        else:
            print("Nenhum texto foi extraído do PDF.")
            return []
            
    except FileNotFoundError as e:
        print(f"Erro: {e}")
        return []
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return []


if __name__ == "__main__":
    main()
