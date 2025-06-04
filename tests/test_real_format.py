#!/usr/bin/env python3
"""
Teste com o formato real do PDF do usuário
"""

import sys
import os

# Adiciona o diretório src ao path para importar os módulos
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from ocr_pdf_reader.text_processor import process_text_lines


def test_real_format():
    """
    Testa o processamento com o formato real do PDF.
    """
    # Simula parte do texto real extraído do PDF
    texto_real = """11.01.39 - INSTITUTO DE ESTUDOS DA AFRICA - GR 11.01.42 - COORDENAÇÃO ADMINISTRATIVA - GR 11.01.55 - DIVISÃO DE ANÁLISE DE PROCESSOS - GR 11.01.56 - DIVISÃO DE PROTOCOLO - GR 11.01.84 - DIVISÃO DE ANÁLISE E ACOMPANHAMENTO DE CONTRATOS E CONVÊNIOS - GR 11.01,44 - DIVISÃO DE APOIO À TECNOLOGIA DA INFORMAÇÃO - GR 11.01.45 - OFICINA DE INFORMATICA - GR 11.01.46 - SERVICO DE TRANSPORTE DA REITORIA 11.01.48 - SECRETARIA DE PROGRAMAS DE EDUCAÇÃO ABERTA E DIGITAL - GR"""
    
    print("TEXTO ORIGINAL (formato real):")
    print("=" * 60)
    print(texto_real[:200] + "...")
    
    # Processa o texto
    linhas_processadas = process_text_lines(texto_real)
    
    print(f"\nTEXTO PROCESSADO ({len(linhas_processadas)} linhas):")
    print("=" * 60)
    for i, linha in enumerate(linhas_processadas[:10], 1):  # Mostra apenas as primeiras 10
        print(f"{i:2d}: {linha}")
    
    if len(linhas_processadas) > 10:
        print(f"... e mais {len(linhas_processadas) - 10} linhas")
    
    return linhas_processadas


def test_with_actual_file():
    """
    Testa com o arquivo real extraído.
    """
    print("\n" + "=" * 60)
    print("TESTANDO COM ARQUIVO REAL")
    print("=" * 60)
    
    try:
        with open('texto_extraido.txt', 'r', encoding='utf-8') as f:
            texto_completo = f.read()
        
        # Processa o texto
        linhas_processadas = process_text_lines(texto_completo)
        
        print(f"Total de linhas processadas: {len(linhas_processadas)}")
        print("\nPrimeiras 10 linhas processadas:")
        print("-" * 40)
        
        for i, linha in enumerate(linhas_processadas[:10], 1):
            print(f"{i:2d}: {linha}")
        
        if len(linhas_processadas) > 10:
            print(f"\n... e mais {len(linhas_processadas) - 10} linhas")
        
        # Salva o resultado processado
        with open('resultado_corrigido.txt', 'w', encoding='utf-8') as f:
            for linha in linhas_processadas:
                f.write(linha + '\n')
        
        print(f"\n✅ Resultado salvo em 'resultado_corrigido.txt'")
        return linhas_processadas
        
    except FileNotFoundError:
        print("❌ Arquivo 'texto_extraido.txt' não encontrado!")
        return []


if __name__ == "__main__":
    print("🧪 TESTANDO PROCESSAMENTO COM FORMATO REAL")
    print("=" * 60)
    
    # Teste com amostra
    linhas_amostra = test_real_format()
    
    # Teste com arquivo completo
    linhas_completo = test_with_actual_file()
    
    print(f"\n✅ Teste concluído!")
    print(f"Amostra: {len(linhas_amostra)} linhas")
    print(f"Arquivo completo: {len(linhas_completo)} linhas") 