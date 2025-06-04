# OCR PDF Reader

Um script Python para extrair texto de arquivos PDF que contêm imagens usando OCR (Optical Character Recognition).

## Funcionalidades

- ✅ Extrai imagens de arquivos PDF
- ✅ Aplica OCR para converter imagens em texto
- ✅ Processa texto para remover números e manter apenas o conteúdo após "-"
- ✅ Remove caracteres não-alfabéticos no final das linhas automaticamente
- ✅ Suporte a português (configurável para outros idiomas)
- ✅ Pré-processamento de imagens para melhor qualidade do OCR
- ✅ Retorna array de strings com o texto extraído

## Pré-requisitos

### 1. Tesseract OCR

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install tesseract-ocr tesseract-ocr-por
```

**Windows:**
- Baixe de: https://github.com/UB-Mannheim/tesseract/wiki

**macOS:**
```bash
brew install tesseract
```

### 2. Dependências Python

As dependências já estão configuradas no projeto. Execute:

```bash
uv sync
```

## Como usar

### 1. Como pacote Python (Recomendado)

```bash
# Instalar as dependências
uv sync

# Usar via linha de comando
uv run python -m ocr_pdf_reader arquivo.pdf
uv run python -m ocr_pdf_reader arquivo.pdf -o resultado.txt --lang por
```

### 2. Modo Interativo

```bash
# Script de compatibilidade
python main.py

# Ou como módulo
uv run python -m ocr_pdf_reader
```

### 3. Modo Programático

```python
from ocr_pdf_reader import extract_text_from_pdf

# Extrai texto do PDF
linhas_texto = extract_text_from_pdf("seu_arquivo.pdf", lang='por')

# O resultado é uma lista de strings
for linha in linhas_texto:
    print(linha)
```

### 4. Usando módulos específicos

```python
from ocr_pdf_reader.core import extract_and_save
from ocr_pdf_reader.text_processor import process_text_lines
from ocr_pdf_reader.image_processor import extract_images_from_pdf

# Extrai e salva diretamente
linhas = extract_and_save("seu_arquivo.pdf", "resultado.txt")
```

### Exemplo Completo

Veja o arquivo `example.py` para um exemplo detalhado de uso.

### Testando a Funcionalidade

Para testar o processamento de linhas quebradas:

```bash
python test_line_breaking.py
```

## Formato de Entrada Esperado

O script processa PDFs onde cada linha de texto segue padrões como:

**Formato simples:**
```
1 - Primeiro item de texto
2 - Segundo item de texto
10 - Décimo item de texto
```

**Formato com códigos (como no seu exemplo):**
```
11.01.39 - INSTITUTO DE ESTUDOS DA AFRICA - GR
11.01.42 - COORDENAÇÃO ADMINISTRATIVA - GR
11.01.55 - DIVISÃO DE ANÁLISE DE PROCESSOS - GR
```

O script extrairá apenas o texto relevante:
```
INSTITUTO DE ESTUDOS DA AFRICA
COORDENAÇÃO ADMINISTRATIVA
DIVISÃO DE ANÁLISE DE PROCESSOS
```

### ✨ Tratamento de Linhas Quebradas

O script agora lida inteligentemente com linhas quebradas pelo OCR:

**Entrada (com linhas quebradas):**
```
1 - Este é um texto muito longo que foi
quebrado em múltiplas linhas pelo OCR
2 - Segundo item também pode estar
quebrado em várias linhas
```

**Saída (linhas unificadas):**
```
Este é um texto muito longo que foi quebrado em múltiplas linhas pelo OCR
Segundo item também pode estar quebrado em várias linhas
```

### 🧹 Limpeza Automática de Caracteres

O script remove automaticamente caracteres não-alfabéticos no final das linhas:

**Entrada (com caracteres problemáticos):**
```
11.01.39 - INSTITUTO DE ESTUDOS DA AFRICA - GR]
11.01.42 - COORDENAÇÃO ADMINISTRATIVA - GR1
11.01.55 - DIVISÃO DE PROTOCOLO - CCsA)
```

**Saída (caracteres removidos):**
```
INSTITUTO DE ESTUDOS DA AFRICA - GR
COORDENAÇÃO ADMINISTRATIVA - GR
DIVISÃO DE PROTOCOLO - CCsA
```

## Estrutura do Projeto

```
ocr-pdf-reader/
├── src/
│   └── ocr_pdf_reader/          # Pacote principal
│       ├── __init__.py          # Inicialização do pacote
│       ├── __main__.py          # Ponto de entrada principal
│       ├── core.py              # Funções principais
│       ├── cli.py               # Interface de linha de comando
│       ├── image_processor.py   # Processamento de imagens
│       └── text_processor.py    # Processamento de texto
├── tests/                       # Testes unitários
│   ├── __init__.py
│   ├── test_text_processor.py
│   ├── test_line_breaking.py
│   └── test_real_format.py
├── examples/                    # Exemplos de uso
│   └── example.py
├── config/                      # Configurações
│   └── settings.py
├── docs/                        # Documentação adicional
├── main.py                      # Script de compatibilidade
├── pyproject.toml              # Configuração do projeto
├── README.md                   # Documentação
└── texto_extraido.txt          # Arquivo de saída (gerado automaticamente)
```

## Funções Principais

### `extract_text_from_pdf(pdf_path, lang='por')`

Função principal que extrai texto de um PDF.

**Parâmetros:**
- `pdf_path` (str): Caminho para o arquivo PDF
- `lang` (str): Idioma para OCR (padrão: 'por')

**Retorna:**
- `List[str]`: Lista com as linhas de texto extraídas

### `extract_images_from_pdf(pdf_path)`

Extrai todas as imagens de um PDF.

### `process_text_lines(text)`

Processa texto bruto do OCR, removendo números e mantendo apenas o conteúdo após "-".

## Configurações de OCR

O script usa as seguintes configurações do Tesseract:
- **OEM 3**: LSTM OCR Engine
- **PSM 6**: Bloco uniforme de texto
- **Idioma padrão**: Português ('por')

## Tratamento de Erros

- ✅ Verifica se o arquivo PDF existe
- ✅ Trata erros de OCR graciosamente
- ✅ Pré-processamento de imagem para melhor qualidade
- ✅ Mensagens informativas durante o processamento

## Limitações

- Requer Tesseract instalado no sistema
- Qualidade do OCR depende da resolução e clareza das imagens
- Funciona melhor com texto em formato de lista numerada

## Contribuindo

Sinta-se livre para abrir issues ou enviar pull requests com melhorias!

## Licença

MIT License
