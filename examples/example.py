#!/usr/bin/env python3
"""
Usage example of the OCR PDF Reader
"""

from main import extract_text_from_pdf


def usage_example():
    """
    Example of how to use the script programmatically.
    """
    # Path to the PDF
    pdf_path = "./doc.pdf"
    
    try:
        # Extract text
        text_lines = extract_text_from_pdf(pdf_path, lang='eng')
        
        # Process the result
        if text_lines:
            print("Text extracted successfully!")
            print(f"Total lines: {len(text_lines)}")
            
            # Example: search for lines containing a specific word
            search_word = "example"
            filtered_lines = [line for line in text_lines if search_word.lower() in line.lower()]
            
            if filtered_lines:
                print(f"\nLines containing '{search_word}':")
                for line in filtered_lines:
                    print(f"- {line}")
            
            # Return the array of strings
            return text_lines
        else:
            print("No text was extracted.")
            return []
            
    except Exception as e:
        print(f"Error: {e}")
        return []


if __name__ == "__main__":
    result = usage_example()
    
    # The result is an array of strings with the extracted text
    print(f"\nResult type: {type(result)}")
    print(f"Number of elements: {len(result)}") 