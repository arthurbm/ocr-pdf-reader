# OCR PDF Reader

A Python script to extract text from PDF files containing images using OCR (Optical Character Recognition).

## Features

- ✅ Extract images from PDF files
- ✅ Apply OCR to convert images to text
- ✅ Process text to remove numbers and keep only content after "-"
- ✅ Automatically remove non-alphabetic characters at end of lines
- ✅ Support for English (configurable for other languages)
- ✅ Image preprocessing for better OCR quality
- ✅ Returns array of strings with extracted text

## Prerequisites

### 1. Tesseract OCR

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install tesseract-ocr tesseract-ocr-eng
```

**Windows:**
- Download from: https://github.com/UB-Mannheim/tesseract/wiki

**macOS:**
```bash
brew install tesseract
```

### 2. Python Dependencies

Dependencies are already configured in the project. Run:

```bash
uv sync
```

## How to Use

### 1. As Python Package (Recommended)

```bash
# Install dependencies
uv sync

# Use via command line
uv run python -m ocr_pdf_reader file.pdf
uv run python -m ocr_pdf_reader file.pdf -o result.txt --lang eng
```

### 2. Interactive Mode

```bash
# Compatibility script
python main.py

# Or as module
uv run python -m ocr_pdf_reader
```

### 3. Programmatic Mode

```python
from ocr_pdf_reader import extract_text_from_pdf

# Extract text from PDF
text_lines = extract_text_from_pdf("your_file.pdf", lang='eng')

# Result is a list of strings
for line in text_lines:
    print(line)
```

### 4. Using Specific Modules

```python
from ocr_pdf_reader.core import extract_and_save
from ocr_pdf_reader.text_processor import process_text_lines
from ocr_pdf_reader.image_processor import extract_images_from_pdf

# Extract and save directly
lines = extract_and_save("your_file.pdf", "result.txt")
```

### Complete Example

See the `example.py` file for a detailed usage example.

### Testing Functionality

To test broken line processing:

```bash
python test_line_breaking.py
```

## Expected Input Format

The script processes PDFs where each text line follows patterns like:

**Simple format:**
```
1 - First text item
2 - Second text item
10 - Tenth text item
```

**Format with codes (like in your example):**
```
11.01.39 - INSTITUTE OF AFRICAN STUDIES - GR
11.01.42 - ADMINISTRATIVE COORDINATION - GR
11.01.55 - PROCESS ANALYSIS DIVISION - GR
```

The script will extract only the relevant text:
```
INSTITUTE OF AFRICAN STUDIES
ADMINISTRATIVE COORDINATION
PROCESS ANALYSIS DIVISION
```

### ✨ Broken Line Handling

The script now intelligently handles lines broken by OCR:

**Input (with broken lines):**
```
1 - This is a very long text that was
broken into multiple lines by OCR
2 - Second item can also be
broken into several lines
```

**Output (unified lines):**
```
This is a very long text that was broken into multiple lines by OCR
Second item can also be broken into several lines
```

### 🧹 Automatic Character Cleaning

The script automatically removes non-alphabetic characters at the end of lines:

**Input (with problematic characters):**
```
11.01.39 - INSTITUTE OF AFRICAN STUDIES - GR]
11.01.42 - ADMINISTRATIVE COORDINATION - GR1
11.01.55 - PROTOCOL DIVISION - CCsA)
```

**Output (characters removed):**
```
INSTITUTE OF AFRICAN STUDIES - GR
ADMINISTRATIVE COORDINATION - GR
PROTOCOL DIVISION - CCsA
```

## Project Structure

```
ocr-pdf-reader/
├── src/
│   └── ocr_pdf_reader/          # Main package
│       ├── __init__.py          # Package initialization
│       ├── __main__.py          # Main entry point
│       ├── core.py              # Main functions
│       ├── cli.py               # Command line interface
│       ├── image_processor.py   # Image processing
│       └── text_processor.py    # Text processing
├── tests/                       # Unit tests
│   ├── __init__.py
│   ├── test_text_processor.py
│   ├── test_line_breaking.py
│   └── test_real_format.py
├── examples/                    # Usage examples
│   └── example.py
├── config/                      # Configurations
│   └── settings.py
├── docs/                        # Additional documentation
├── main.py                      # Compatibility script
├── pyproject.toml              # Project configuration
├── README.md                   # Documentation
└── extracted_text.txt          # Output file (generated automatically)
```

## Main Functions

### `extract_text_from_pdf(pdf_path, lang='eng')`

Main function that extracts text from a PDF.

**Parameters:**
- `pdf_path` (str): Path to the PDF file
- `lang` (str): Language for OCR (default: 'eng')

**Returns:**
- `List[str]`: List of extracted text lines

### `extract_images_from_pdf(pdf_path)`

Extracts all images from a PDF.

### `process_text_lines(text)`

Processes raw OCR text, removing numbers and keeping only content after "-".

## OCR Settings

The script uses the following Tesseract settings:
- **OEM 3**: LSTM OCR Engine
- **PSM 6**: Uniform block of text
- **Default language**: English ('eng')

## Error Handling

- ✅ Checks if PDF file exists
- ✅ Handles OCR errors gracefully
- ✅ Image preprocessing for better quality
- ✅ Informative messages during processing

## Limitations

- Requires Tesseract installed on system
- OCR quality depends on image resolution and clarity
- Works best with numbered list format text

## Contributing

Feel free to open issues or submit pull requests with improvements!

## License

MIT License
