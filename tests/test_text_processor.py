"""
Unit tests for the text_processor module.
"""

import unittest
import sys
import os

# Add src directory to path to import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from ocr_pdf_reader.text_processor import process_text_lines, validate_extracted_lines, remove_non_letter_ending


class TestTextProcessor(unittest.TestCase):
    """Tests for the text processor."""
    
    def test_process_text_lines_standard_format(self):
        """Test processing with standard format."""
        text = "11.01.39 - INSTITUTE OF AFRICAN STUDIES - GR 11.01.42 - ADMINISTRATIVE COORDINATION - GR"
        result = process_text_lines(text)
        
        expected = [
            "INSTITUTE OF AFRICAN STUDIES - GR",
            "ADMINISTRATIVE COORDINATION - GR"
        ]
        
        self.assertEqual(result, expected)
    
    def test_process_text_lines_with_acronyms(self):
        """Test if it maintains acronyms at the end."""
        text = "11.01.55 - PROCESS ANALYSIS DIVISION - GR 11.01.56 - PROTOCOL DIVISION - CCsA"
        result = process_text_lines(text)
        
        # Should maintain acronyms
        self.assertTrue(any("- GR" in line for line in result))
        self.assertTrue(any("- CCsA" in line for line in result))
    
    def test_process_text_lines_simple_format(self):
        """Test processing with simple format."""
        text = "1 - First item 2 - Second item 3 - Third item"
        result = process_text_lines(text)
        
        expected = [
            "First item",
            "Second item", 
            "Third item"
        ]
        
        self.assertEqual(result, expected)
    
    def test_validate_extracted_lines(self):
        """Test validation of extracted lines."""
        lines = [
            "INSTITUTE OF AFRICAN STUDIES",
            "AB",  # Too short
            "123456",  # Only numbers
            "ADMINISTRATIVE COORDINATION",
            "",  # Empty
            "PROTOCOL DIVISION"
        ]
        
        result = validate_extracted_lines(lines)
        
        expected = [
            "INSTITUTE OF AFRICAN STUDIES",
            "ADMINISTRATIVE COORDINATION", 
            "PROTOCOL DIVISION"
        ]
        
        self.assertEqual(result, expected)
    
    def test_remove_duplicates(self):
        """Test duplicate removal."""
        text = "1 - TEST 2 - OTHER 3 - TEST"  # TEST duplicated
        result = process_text_lines(text)
        
        # Should have only one "TEST"
        self.assertEqual(result.count("TEST"), 1)
        self.assertIn("OTHER", result)
    
    def test_remove_non_letter_ending(self):
        """Test removal of non-alphabetic characters at the end."""
        # Cases with non-alphabetic characters at the end
        self.assertEqual(remove_non_letter_ending("TEST1"), "TEST")
        self.assertEqual(remove_non_letter_ending("TEST."), "TEST")
        self.assertEqual(remove_non_letter_ending("TEST]"), "TEST")
        self.assertEqual(remove_non_letter_ending("TEST-"), "TEST")
        self.assertEqual(remove_non_letter_ending("TEST )"), "TEST")
        
        # Cases that should remain unchanged
        self.assertEqual(remove_non_letter_ending("TEST"), "TEST")
        self.assertEqual(remove_non_letter_ending("TESTEA"), "TESTEA")
        self.assertEqual(remove_non_letter_ending(""), "")
        
        # Cases with spaces
        self.assertEqual(remove_non_letter_ending("TEST 1 "), "TEST")
        self.assertEqual(remove_non_letter_ending("TEST A "), "TEST A")


if __name__ == '__main__':
    unittest.main() 