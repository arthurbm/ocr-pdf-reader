#!/usr/bin/env python3
"""
Teste da funcionalidade de processamento de linhas quebradas
"""

import sys
import os

# Adiciona o diretório src ao path para importar os módulos
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from ocr_pdf_reader.text_processor import process_text_lines


def test_line_breaking():
    """
    Testa o processamento de linhas quebradas.
    """
    # Simula texto extraído do OCR com linhas quebradas
    texto_ocr = """
1 - Este é o primeiro item que pode ter
uma linha muito longa que foi quebrada
pelo OCR em múltiplas linhas
2 - Este é o segundo item que também
pode estar quebrado em várias linhas
conforme extraído pelo OCR
3 - Terceiro item curto
4 - Quarto item que novamente tem uma
linha bem longa que pode ser quebrada
quando o OCR processa a imagem
5 - Quinto e último item
"""
    
    print("TEXTO ORIGINAL (simulando OCR):")
    print("=" * 50)
    print(texto_ocr)
    
    # Processa o texto
    linhas_processadas = process_text_lines(texto_ocr)
    
    print("\nTEXTO PROCESSADO:")
    print("=" * 50)
    for i, linha in enumerate(linhas_processadas, 1):
        print(f"{i}: {linha}")
    
    return linhas_processadas


def test_edge_cases():
    """
    Testa casos especiais de formatação.
    """
    print("\n" + "=" * 60)
    print("TESTANDO CASOS ESPECIAIS")
    print("=" * 60)
    
    # Teste 1: Números sem traço
    texto1 = """
1 Primeiro item sem traço
continuação da primeira linha
2 Segundo item sem traço
"""
    print("\nTeste 1 - Números sem traço:")
    print("Entrada:", repr(texto1))
    resultado1 = process_text_lines(texto1)
    print("Resultado:", resultado1)
    
    # Teste 2: Formatação mista
    texto2 = """
1. - Item com ponto e traço
continuação desta linha
2) Item com parênteses
mas sem traço
3 - Item normal com traço
e sua continuação
"""
    print("\nTeste 2 - Formatação mista:")
    print("Entrada:", repr(texto2))
    resultado2 = process_text_lines(texto2)
    print("Resultado:", resultado2)
    
    # Teste 3: Linhas em branco e espaços
    texto3 = """
1 - Primeiro item

continuação após linha em branco

2 - Segundo item
   com espaços extras
      e indentação
3 - Terceiro item
"""
    print("\nTeste 3 - Linhas em branco e espaços:")
    print("Entrada:", repr(texto3))
    resultado3 = process_text_lines(texto3)
    print("Resultado:", resultado3)


if __name__ == "__main__":
    # Executa os testes
    print("🧪 TESTANDO PROCESSAMENTO DE LINHAS QUEBRADAS")
    print("=" * 60)
    
    linhas = test_line_breaking()
    test_edge_cases()
    
    print(f"\n✅ Teste concluído! Total de linhas processadas: {len(linhas)}") 