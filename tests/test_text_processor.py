"""
Testes unitários para o módulo text_processor.
"""

import unittest
import sys
import os

# Adiciona o diretório src ao path para importar os módulos
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from ocr_pdf_reader.text_processor import process_text_lines, validate_extracted_lines, remove_non_letter_ending


class TestTextProcessor(unittest.TestCase):
    """Testes para o processador de texto."""
    
    def test_process_text_lines_standard_format(self):
        """Testa processamento com formato padrão."""
        text = "11.01.39 - INSTITUTO DE ESTUDOS DA AFRICA - GR 11.01.42 - COORDENAÇÃO ADMINISTRATIVA - GR"
        result = process_text_lines(text)
        
        expected = [
            "INSTITUTO DE ESTUDOS DA AFRICA - GR",
            "COORDENAÇÃO ADMINISTRATIVA - GR"
        ]
        
        self.assertEqual(result, expected)
    
    def test_process_text_lines_with_acronyms(self):
        """Testa se mantém as siglas no final."""
        text = "11.01.55 - DIVISÃO DE ANÁLISE DE PROCESSOS - GR 11.01.56 - DIVISÃO DE PROTOCOLO - CCsA"
        result = process_text_lines(text)
        
        # Deve manter as siglas
        self.assertTrue(any("- GR" in line for line in result))
        self.assertTrue(any("- CCsA" in line for line in result))
    
    def test_process_text_lines_simple_format(self):
        """Testa processamento com formato simples."""
        text = "1 - Primeiro item 2 - Segundo item 3 - Terceiro item"
        result = process_text_lines(text)
        
        expected = [
            "Primeiro item",
            "Segundo item", 
            "Terceiro item"
        ]
        
        self.assertEqual(result, expected)
    
    def test_validate_extracted_lines(self):
        """Testa validação de linhas extraídas."""
        lines = [
            "INSTITUTO DE ESTUDOS DA AFRICA",
            "AB",  # Muito curta
            "123456",  # Só números
            "COORDENAÇÃO ADMINISTRATIVA",
            "",  # Vazia
            "DIVISÃO DE PROTOCOLO"
        ]
        
        result = validate_extracted_lines(lines)
        
        expected = [
            "INSTITUTO DE ESTUDOS DA AFRICA",
            "COORDENAÇÃO ADMINISTRATIVA", 
            "DIVISÃO DE PROTOCOLO"
        ]
        
        self.assertEqual(result, expected)
    
    def test_remove_duplicates(self):
        """Testa remoção de duplicatas."""
        text = "1 - TESTE 2 - OUTRO 3 - TESTE"  # TESTE duplicado
        result = process_text_lines(text)
        
        # Deve ter apenas um "TESTE"
        self.assertEqual(result.count("TESTE"), 1)
        self.assertIn("OUTRO", result)
    
    def test_remove_non_letter_ending(self):
        """Testa remoção de caracteres não-alfabéticos no final."""
        # Casos com caracteres não-alfabéticos no final
        self.assertEqual(remove_non_letter_ending("TESTE1"), "TESTE")
        self.assertEqual(remove_non_letter_ending("TESTE."), "TESTE")
        self.assertEqual(remove_non_letter_ending("TESTE]"), "TESTE")
        self.assertEqual(remove_non_letter_ending("TESTE-"), "TESTE")
        self.assertEqual(remove_non_letter_ending("TESTE )"), "TESTE")
        
        # Casos que devem permanecer inalterados
        self.assertEqual(remove_non_letter_ending("TESTE"), "TESTE")
        self.assertEqual(remove_non_letter_ending("TESTEA"), "TESTEA")
        self.assertEqual(remove_non_letter_ending(""), "")
        
        # Casos com espaços
        self.assertEqual(remove_non_letter_ending("TESTE 1 "), "TESTE")
        self.assertEqual(remove_non_letter_ending("TESTE A "), "TESTE A")


if __name__ == '__main__':
    unittest.main() 