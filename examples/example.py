#!/usr/bin/env python3
"""
Exemplo de uso do OCR PDF Reader
"""

from main import extract_text_from_pdf


def exemplo_uso():
    """
    Exemplo de como usar o script programaticamente.
    """
    # Caminho para o PDF
    pdf_path = "./doc.pdf"
    
    try:
        # Extrai o texto
        linhas_texto = extract_text_from_pdf(pdf_path, lang='por')
        
        # Processa o resultado
        if linhas_texto:
            print("Texto extraído com sucesso!")
            print(f"Total de linhas: {len(linhas_texto)}")
            
            # Exemplo: buscar linhas que contenham uma palavra específica
            palavra_busca = "exemplo"
            linhas_filtradas = [linha for linha in linhas_texto if palavra_busca.lower() in linha.lower()]
            
            if linhas_filtradas:
                print(f"\nLinhas contendo '{palavra_busca}':")
                for linha in linhas_filtradas:
                    print(f"- {linha}")
            
            # Retorna o array de strings
            return linhas_texto
        else:
            print("Nenhum texto foi extraído.")
            return []
            
    except Exception as e:
        print(f"Erro: {e}")
        return []


if __name__ == "__main__":
    resultado = exemplo_uso()
    
    # O resultado é um array de strings com o texto extraído
    print(f"\nTipo do resultado: {type(resultado)}")
    print(f"Número de elementos: {len(resultado)}") 