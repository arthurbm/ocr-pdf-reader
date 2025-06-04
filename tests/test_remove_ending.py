#!/usr/bin/env python3
"""
Teste específico para a funcionalidade de remoção do último caractere não-alfabético.
"""

import sys
import os

# Adiciona o diretório src ao path para importar os módulos
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from ocr_pdf_reader.text_processor import process_text_lines


def test_remove_ending_in_real_context():
    """
    Testa a remoção do último caractere em contexto real com códigos.
    """
    # Simula texto extraído do OCR com caracteres não-alfabéticos no final
    texto_com_problemas = """
11.01.39 - INSTITUTO DE ESTUDOS DA AFRICA - GR]
11.01.42 - COORDENAÇÃO ADMINISTRATIVA - GR1
11.01.55 - DIVISÃO DE ANÁLISE DE PROCESSOS - GR.
11.01.56 - DIVISÃO DE PROTOCOLO - CCsA)
11.01.84 - SECRETARIA DE PROGRAMAS - PROGEPE2
"""
    
    print("TEXTO ORIGINAL (com caracteres problemáticos no final):")
    print("=" * 60)
    for linha in texto_com_problemas.strip().split('\n'):
        if linha.strip():
            print(f"'{linha.strip()}'")
    
    # Processa o texto
    result = process_text_lines(texto_com_problemas)
    
    print("\nTEXTO PROCESSADO (caracteres problemáticos removidos):")
    print("=" * 60)
    for i, linha in enumerate(result, 1):
        print(f"{i:2d}: '{linha}'")
    
    # Verificações
    expected_endings = ['GR', 'GR', 'GR', 'CCsA', 'PROGEPE']
    
    print("\nVERIFICAÇÕES:")
    print("-" * 30)
    
    for i, linha in enumerate(result):
        if i < len(expected_endings):
            expected_end = expected_endings[i]
            if linha.endswith(expected_end):
                print(f"✅ Linha {i+1}: Termina corretamente com '{expected_end}'")
            else:
                print(f"❌ Linha {i+1}: Deveria terminar com '{expected_end}', mas termina com '{linha[-10:]}'")
        
        # Verifica se o último caractere é uma letra
        if linha and linha[-1].isalpha():
            print(f"✅ Linha {i+1}: Último caractere '{linha[-1]}' é uma letra")
        else:
            print(f"❌ Linha {i+1}: Último caractere '{linha[-1] if linha else 'N/A'}' não é uma letra")
    
    return result


if __name__ == "__main__":
    print("=== TESTE: Remoção de Caracteres Não-Alfabéticos no Final ===\n")
    test_remove_ending_in_real_context()
    print("\n=== FIM DO TESTE ===") 