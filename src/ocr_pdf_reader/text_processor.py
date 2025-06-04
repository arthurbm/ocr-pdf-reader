"""
Module for processing text extracted via OCR.

This module contains functions for:
- Processing raw text extracted from OCR
- Removing numeric codes and keeping only relevant content
- Handling broken lines and continuous text
"""

import re
from typing import List


def process_text_lines(text: str) -> List[str]:
    """
    Processes extracted text, removing numeric codes and keeping only content after "-".
    Handles codes in format "11.01.39 - DESCRIPTION" and continuous text.
    Maintains acronyms at the end of descriptions.
    
    Args:
        text (str): Raw text extracted from OCR
        
    Returns:
        List[str]: List of processed lines without numeric codes
    """
    processed_lines = []
    
    # Pattern for codes in format "XX.XX.XX - TEXT" or "XX.XX - TEXT" or "X - TEXT"
    # Also accepts codes with dots, commas and other separators
    pattern = r'(\d+(?:[\.\,]\d+)*(?:[\.\,]\d+)*)\s*-\s*([^0-9]+?)(?=\s+\d+(?:[\.\,]\d+)*\s*-|\s*$)'
    
    # Remove unnecessary line breaks and join everything in one line
    clean_text = ' '.join(text.split())
    
    # Find all matches
    matches = re.findall(pattern, clean_text)
    
    if matches:
        for code, description in matches:
            # Clean description keeping acronyms at the end
            desc_clean = description.strip()
            
            # Remove only parentheses at the end, but keep acronyms with hyphen
            desc_clean = re.sub(r'\s*\([^)]*\)\s*$', '', desc_clean)
            
            # Remove last character if it's not a letter
            desc_clean = remove_non_letter_ending(desc_clean)
            
            if desc_clean and len(desc_clean.strip()) > 2:
                processed_lines.append(desc_clean.strip())
    else:
        # Fallback: if main pattern doesn't work, try simpler patterns
        # Split by codes that start with digits followed by hyphen
        parts = re.split(r'\s+(?=\d+[\.\,]\d+.*?-)', text)
        
        for part in parts:
            if '-' in part:
                # Take everything after the first hyphen
                after_dash = part.split('-', 1)[1].strip()
                # Keep acronyms, remove only parentheses
                after_dash = re.sub(r'\s*\([^)]*\)\s*$', '', after_dash)
                
                # Remove last character if it's not a letter
                after_dash = remove_non_letter_ending(after_dash)
                
                if after_dash and len(after_dash.strip()) > 2:
                    processed_lines.append(after_dash.strip())
    
    # Remove duplicates maintaining order
    seen = set()
    unique_lines = []
    for line in processed_lines:
        if line not in seen:
            seen.add(line)
            unique_lines.append(line)
    
    return unique_lines


def remove_non_letter_ending(text: str) -> str:
    """
    Removes the last character from string if it's not a letter.
    
    Args:
        text (str): Text to be processed
        
    Returns:
        str: Text with last character removed if it's not a letter
    """
    if not text:
        return text
    
    text = text.strip()
    if text and not text[-1].isalpha():
        return text[:-1].strip()
    
    return text


def clean_text(text: str) -> str:
    """
    Basic text cleaning removing unwanted characters.
    
    Args:
        text (str): Text to be cleaned
        
    Returns:
        str: Cleaned text
    """
    # Remove extra spaces
    text = ' '.join(text.split())
    
    # Remove control characters
    text = ''.join(char for char in text if ord(char) >= 32 or char in '\n\t')
    
    return text.strip()


def validate_extracted_lines(lines: List[str], min_length: int = 3) -> List[str]:
    """
    Validates and filters extracted lines based on minimum criteria.
    
    Args:
        lines (List[str]): List of lines to validate
        min_length (int): Minimum length of a valid line
        
    Returns:
        List[str]: List of valid lines
    """
    valid_lines = []
    
    for line in lines:
        # Remove spaces and check minimum length
        clean_line = line.strip()
        
        if len(clean_line) >= min_length:
            # Check if it's not just numbers or special characters
            if any(char.isalpha() for char in clean_line):
                valid_lines.append(clean_line)
    
    return valid_lines 