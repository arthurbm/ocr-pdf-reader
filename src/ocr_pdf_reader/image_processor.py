"""
Module for image processing and text extraction via OCR.

This module contains functions for:
- Extracting images from PDF files
- Preprocessing images to improve OCR quality
- Applying OCR to images to extract text
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
    Preprocesses the image to improve OCR quality.
    
    Args:
        image_array (np.ndarray): Image array to be processed
        
    Returns:
        np.ndarray: Processed image
    """
    # Convert to grayscale if necessary
    if len(image_array.shape) == 3:
        gray = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)
    else:
        gray = image_array
    
    # Apply threshold to improve contrast
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Remove noise
    kernel = np.ones((1, 1), np.uint8)
    cleaned = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    
    return cleaned


def extract_images_from_pdf(pdf_path: str) -> List[Image.Image]:
    """
    Extracts all images from a PDF file.
    
    Args:
        pdf_path (str): Path to the PDF file
        
    Returns:
        List[Image.Image]: List of extracted images
        
    Raises:
        FileNotFoundError: If the PDF file is not found
    """
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")
    
    images = []
    pdf_document = fitz.open(pdf_path)
    
    try:
        for page_num in range(len(pdf_document)):
            page = pdf_document[page_num]
            image_list = page.get_images()
            
            for img_index, img in enumerate(image_list):
                # Extract the image
                xref = img[0]
                pix = fitz.Pixmap(pdf_document, xref)
                
                if pix.n - pix.alpha < 4:  # GRAY or RGB
                    img_data = pix.tobytes("ppm")
                    img_pil = Image.open(io.BytesIO(img_data))
                    images.append(img_pil)
                
                pix = None
            
            # If no embedded images found, render page as image
            if not image_list:
                mat = fitz.Matrix(2.0, 2.0)  # Increase resolution
                pix = page.get_pixmap(matrix=mat)
                img_data = pix.tobytes("ppm")
                img_pil = Image.open(io.BytesIO(img_data))
                images.append(img_pil)
                pix = None
    
    finally:
        pdf_document.close()
    
    return images


def extract_text_from_image(image: Image.Image, lang: str = 'eng') -> str:
    """
    Extracts text from an image using OCR.
    
    Args:
        image (Image.Image): Image to extract text from
        lang (str): Language for OCR (default: 'eng' for English)
        
    Returns:
        str: Text extracted from the image
    """
    try:
        # Convert PIL to numpy array
        img_array = np.array(image)
        
        # Preprocess the image
        processed_img = preprocess_image(img_array)
        
        # Apply OCR
        custom_config = r'--oem 3 --psm 6'
        text = pytesseract.image_to_string(processed_img, lang=lang, config=custom_config)
        
        return text
    except Exception as e:
        print(f"Error extracting text from image: {e}")
        return ""


def check_tesseract_installation() -> bool:
    """
    Checks if Tesseract OCR is installed and accessible.
    
    Returns:
        bool: True if Tesseract is available, False otherwise
    """
    try:
        pytesseract.get_tesseract_version()
        return True
    except Exception:
        return False 