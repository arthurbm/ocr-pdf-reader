"""
Módulo para processamento de imagens e extração de texto via OCR.

Este módulo contém funções para:
- Extrair imagens de arquivos PDF
- Pré-processar imagens para melhorar a qualidade do OCR
- Aplicar OCR em imagens para extrair texto
"""

import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import cv2
import numpy as np
import io
import os
from typing import List


def preprocess_image(image_array: np.ndarray) -> np.ndarray:
    """
    Pré-processa a imagem para melhorar a qualidade do OCR.
    
    Args:
        image_array (np.ndarray): Array da imagem a ser processada
        
    Returns:
        np.ndarray: Imagem processada
    """
    # Converte para escala de cinza se necessário
    if len(image_array.shape) == 3:
        gray = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)
    else:
        gray = image_array
    
    # Aplica threshold para melhorar o contraste
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Remove ruído
    kernel = np.ones((1, 1), np.uint8)
    cleaned = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    
    return cleaned


def extract_images_from_pdf(pdf_path: str) -> List[Image.Image]:
    """
    Extrai todas as imagens de um arquivo PDF.
    
    Args:
        pdf_path (str): Caminho para o arquivo PDF
        
    Returns:
        List[Image.Image]: Lista de imagens extraídas
        
    Raises:
        FileNotFoundError: Se o arquivo PDF não for encontrado
    """
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"Arquivo PDF não encontrado: {pdf_path}")
    
    images = []
    pdf_document = fitz.open(pdf_path)
    
    try:
        for page_num in range(len(pdf_document)):
            page = pdf_document[page_num]
            image_list = page.get_images()
            
            for img_index, img in enumerate(image_list):
                # Extrai a imagem
                xref = img[0]
                pix = fitz.Pixmap(pdf_document, xref)
                
                if pix.n - pix.alpha < 4:  # GRAY ou RGB
                    img_data = pix.tobytes("ppm")
                    img_pil = Image.open(io.BytesIO(img_data))
                    images.append(img_pil)
                
                pix = None
            
            # Se não encontrou imagens incorporadas, renderiza a página como imagem
            if not image_list:
                mat = fitz.Matrix(2.0, 2.0)  # Aumenta a resolução
                pix = page.get_pixmap(matrix=mat)
                img_data = pix.tobytes("ppm")
                img_pil = Image.open(io.BytesIO(img_data))
                images.append(img_pil)
                pix = None
    
    finally:
        pdf_document.close()
    
    return images


def extract_text_from_image(image: Image.Image, lang: str = 'por') -> str:
    """
    Extrai texto de uma imagem usando OCR.
    
    Args:
        image (Image.Image): Imagem para extrair texto
        lang (str): Idioma para o OCR (padrão: 'por' para português)
        
    Returns:
        str: Texto extraído da imagem
    """
    try:
        # Converte PIL para numpy array
        img_array = np.array(image)
        
        # Pré-processa a imagem
        processed_img = preprocess_image(img_array)
        
        # Aplica OCR
        custom_config = r'--oem 3 --psm 6'
        text = pytesseract.image_to_string(processed_img, lang=lang, config=custom_config)
        
        return text
    except Exception as e:
        print(f"Erro ao extrair texto da imagem: {e}")
        return ""


def check_tesseract_installation() -> bool:
    """
    Verifica se o Tesseract OCR está instalado e acessível.
    
    Returns:
        bool: True se o Tesseract estiver disponível, False caso contrário
    """
    try:
        pytesseract.get_tesseract_version()
        return True
    except Exception:
        return False 