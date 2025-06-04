"""
Main module of the OCR PDF Reader.

This module integrates all functionalities to extract text from PDFs containing images.
"""

from typing import List
from .image_processor import extract_images_from_pdf, extract_text_from_image
from .text_processor import process_text_lines, validate_extracted_lines


def extract_text_from_pdf(pdf_path: str, lang: str = 'eng', validate: bool = True) -> List[str]:
    """
    Main function that extracts text from a PDF containing images.
    
    Args:
        pdf_path (str): Path to the PDF file
        lang (str): Language for OCR (default: 'eng' for English)
        validate (bool): Whether to validate extracted lines (default: True)
    
    Returns:
        List[str]: List of extracted text lines (without numbers)
        
    Raises:
        FileNotFoundError: If the PDF file is not found
    """
    print(f"Extracting images from PDF: {pdf_path}")
    images = extract_images_from_pdf(pdf_path)
    
    if not images:
        print("No images found in the PDF.")
        return []
    
    print(f"Found {len(images)} image(s). Applying OCR...")
    
    all_text_lines = []
    
    for i, image in enumerate(images):
        print(f"Processing image {i+1}/{len(images)}...")
        
        # Extract text from image
        raw_text = extract_text_from_image(image, lang)
        
        if raw_text:
            # Process text to extract only relevant content
            processed_lines = process_text_lines(raw_text)
            all_text_lines.extend(processed_lines)
    
    # Validate lines if requested
    if validate:
        all_text_lines = validate_extracted_lines(all_text_lines)
    
    return all_text_lines


def extract_and_save(pdf_path: str, output_file: str = "extracted_text.txt", 
                    lang: str = 'eng', validate: bool = True) -> List[str]:
    """
    Extracts text from a PDF and saves to file.
    
    Args:
        pdf_path (str): Path to the PDF file
        output_file (str): Output file name
        lang (str): Language for OCR
        validate (bool): Whether to validate extracted lines
        
    Returns:
        List[str]: List of extracted text lines
    """
    text_lines = extract_text_from_pdf(pdf_path, lang, validate)
    
    if text_lines:
        with open(output_file, 'w', encoding='utf-8') as f:
            for line in text_lines:
                f.write(line + '\n')
        
        print(f"Text saved to: {output_file}")
    
    return text_lines 