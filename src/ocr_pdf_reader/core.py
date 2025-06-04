"""
Módulo principal do OCR PDF Reader.

Este módulo integra todas as funcionalidades para extrair texto de PDFs contendo imagens.
"""

from typing import List
from .image_processor import extract_images_from_pdf, extract_text_from_image
from .text_processor import process_text_lines, validate_extracted_lines


def extract_text_from_pdf(pdf_path: str, lang: str = 'por', validate: bool = True) -> List[str]:
    """
    Função principal que extrai texto de um PDF contendo imagens.
    
    Args:
        pdf_path (str): Caminho para o arquivo PDF
        lang (str): Idioma para o OCR (padrão: 'por' para português)
        validate (bool): Se deve validar as linhas extraídas (padrão: True)
    
    Returns:
        List[str]: Lista com as linhas de texto extraídas (sem os números)
        
    Raises:
        FileNotFoundError: Se o arquivo PDF não for encontrado
    """
    print(f"Extraindo imagens do PDF: {pdf_path}")
    images = extract_images_from_pdf(pdf_path)
    
    if not images:
        print("Nenhuma imagem encontrada no PDF.")
        return []
    
    print(f"Encontradas {len(images)} imagem(ns). Aplicando OCR...")
    
    all_text_lines = []
    
    for i, image in enumerate(images):
        print(f"Processando imagem {i+1}/{len(images)}...")
        
        # Extrai texto da imagem
        raw_text = extract_text_from_image(image, lang)
        
        if raw_text:
            # Processa o texto para extrair apenas o conteúdo relevante
            processed_lines = process_text_lines(raw_text)
            all_text_lines.extend(processed_lines)
    
    # Valida as linhas se solicitado
    if validate:
        all_text_lines = validate_extracted_lines(all_text_lines)
    
    return all_text_lines


def extract_and_save(pdf_path: str, output_file: str = "texto_extraido.txt", 
                    lang: str = 'por', validate: bool = True) -> List[str]:
    """
    Extrai texto de um PDF e salva em arquivo.
    
    Args:
        pdf_path (str): Caminho para o arquivo PDF
        output_file (str): Nome do arquivo de saída
        lang (str): Idioma para o OCR
        validate (bool): Se deve validar as linhas extraídas
        
    Returns:
        List[str]: Lista com as linhas de texto extraídas
    """
    text_lines = extract_text_from_pdf(pdf_path, lang, validate)
    
    if text_lines:
        with open(output_file, 'w', encoding='utf-8') as f:
            for line in text_lines:
                f.write(line + '\n')
        
        print(f"Texto salvo em: {output_file}")
    
    return text_lines 