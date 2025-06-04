"""
Módulo para processamento de texto extraído via OCR.

Este módulo contém funções para:
- Processar texto bruto extraído do OCR
- Remover códigos numéricos e manter apenas o conteúdo relevante
- Lidar com linhas quebradas e texto corrido
"""

import re
from typing import List


def process_text_lines(text: str) -> List[str]:
    """
    Processa o texto extraído, removendo códigos numéricos e mantendo apenas o conteúdo após o "-".
    Lida com códigos no formato "11.01.39 - DESCRIÇÃO" e texto corrido.
    Mantém as siglas no final das descrições.
    
    Args:
        text (str): Texto bruto extraído do OCR
        
    Returns:
        List[str]: Lista de linhas processadas sem os códigos numéricos
    """
    processed_lines = []
    
    # Padrão para códigos no formato "XX.XX.XX - TEXTO" ou "XX.XX - TEXTO" ou "X - TEXTO"
    # Também aceita códigos com pontos, vírgulas e outros separadores
    pattern = r'(\d+(?:[\.\,]\d+)*(?:[\.\,]\d+)*)\s*-\s*([^0-9]+?)(?=\s+\d+(?:[\.\,]\d+)*\s*-|\s*$)'
    
    # Remove quebras de linha desnecessárias e junta tudo em uma linha
    clean_text = ' '.join(text.split())
    
    # Encontra todas as correspondências
    matches = re.findall(pattern, clean_text)
    
    if matches:
        for code, description in matches:
            # Limpa a descrição mantendo as siglas no final
            desc_clean = description.strip()
            
            # Remove apenas parênteses no final, mas mantém as siglas com hífen
            desc_clean = re.sub(r'\s*\([^)]*\)\s*$', '', desc_clean)
            
            # Remove o último caractere se não for uma letra
            desc_clean = remove_non_letter_ending(desc_clean)
            
            if desc_clean and len(desc_clean.strip()) > 2:
                processed_lines.append(desc_clean.strip())
    else:
        # Fallback: se o padrão principal não funcionar, tenta padrões mais simples
        # Divide por códigos que começam com dígitos seguidos de hífen
        parts = re.split(r'\s+(?=\d+[\.\,]\d+.*?-)', text)
        
        for part in parts:
            if '-' in part:
                # Pega tudo após o primeiro hífen
                after_dash = part.split('-', 1)[1].strip()
                # Mantém as siglas, remove apenas parênteses
                after_dash = re.sub(r'\s*\([^)]*\)\s*$', '', after_dash)
                
                # Remove o último caractere se não for uma letra
                after_dash = remove_non_letter_ending(after_dash)
                
                if after_dash and len(after_dash.strip()) > 2:
                    processed_lines.append(after_dash.strip())
    
    # Remove duplicatas mantendo a ordem
    seen = set()
    unique_lines = []
    for line in processed_lines:
        if line not in seen:
            seen.add(line)
            unique_lines.append(line)
    
    return unique_lines


def remove_non_letter_ending(text: str) -> str:
    """
    Remove o último caractere da string se ele não for uma letra.
    
    Args:
        text (str): Texto a ser processado
        
    Returns:
        str: Texto com último caractere removido se não for letra
    """
    if not text:
        return text
    
    text = text.strip()
    if text and not text[-1].isalpha():
        return text[:-1].strip()
    
    return text


def clean_text(text: str) -> str:
    """
    Limpa texto básico removendo caracteres indesejados.
    
    Args:
        text (str): Texto a ser limpo
        
    Returns:
        str: Texto limpo
    """
    # Remove espaços extras
    text = ' '.join(text.split())
    
    # Remove caracteres de controle
    text = ''.join(char for char in text if ord(char) >= 32 or char in '\n\t')
    
    return text.strip()


def validate_extracted_lines(lines: List[str], min_length: int = 3) -> List[str]:
    """
    Valida e filtra linhas extraídas com base em critérios mínimos.
    
    Args:
        lines (List[str]): Lista de linhas para validar
        min_length (int): Comprimento mínimo de uma linha válida
        
    Returns:
        List[str]: Lista de linhas válidas
    """
    valid_lines = []
    
    for line in lines:
        # Remove espaços e verifica comprimento mínimo
        clean_line = line.strip()
        
        if len(clean_line) >= min_length:
            # Verifica se não é apenas números ou caracteres especiais
            if any(char.isalpha() for char in clean_line):
                valid_lines.append(clean_line)
    
    return valid_lines 