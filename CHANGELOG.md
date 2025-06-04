# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-12-31

### 🎉 First Stable Release

### Added
- ✨ **Complete modular architecture**
  - Separation into specialized modules (`core`, `image_processor`, `text_processor`, `cli`)
  - Professional Python package structure
  - Centralized configurations

- 🚀 **Multiple usage interfaces**
  - Command line interface (CLI) with arguments
  - Interactive mode for beginners  
  - Programmatic API for developers
  - Compatibility script (`main.py`)

- 🧠 **Intelligent text processing**
  - Automatic detection of codes in format "XX.XX.XX - DESCRIPTION"
  - Maintenance of organizational acronyms (e.g. "- GR", "- CCsA")
  - Handling of lines broken by OCR
  - Automatic text validation and cleaning

- 📦 **Modern dependency management**
  - Configuration with `pyproject.toml`
  - Full UV support (Python package manager)
  - Versioned and compatible dependencies

- 🧪 **Testing and quality**
  - Unit tests for critical functionalities
  - Organized test structure
  - Configuration for quality tools (Black, Flake8, MyPy)

- 📚 **Complete documentation**
  - Detailed README with examples
  - Architecture documentation (ARCHITECTURE.md)
  - Programmatic usage examples
  - Makefile with useful commands

- ⚙️ **Flexible configurations**
  - Configurable regex patterns for different formats
  - Adjustable OCR parameters
  - Support for multiple languages
  - Configurable logging system

### Core Features
- 🔍 **PDF image extraction** using PyMuPDF
- 👁️ **OCR with Tesseract** and image preprocessing
- 📝 **Intelligent processing** of extracted text
- 🎯 **Clean results** without numeric codes, keeping only descriptions
- 🔧 **Compatibility** maintained with previous version

### Technical Improvements
- Type hints in all functions
- Complete docstrings
- Robust error handling
- Structured logging
- Code following PEP 8
- Extensible architecture

### Supported Formats
- PDFs with embedded images
- PDFs rendered as image
- Code formats: "X - TEXT", "XX.XX - TEXT", "XX.XX.XX - TEXT"
- Continuous text and broken lines

### Requirements
- Python 3.9+
- Tesseract OCR installed on system
- Dependencies: PyMuPDF, pytesseract, Pillow, opencv-python

## [0.1.0] - 2024-12-30

### Initial Development
- 🚀 **First functional version**
- ✅ Basic text extraction from PDFs
- ✅ Simple processing of numbered lines
- ✅ Monolithic script in `main.py`

---

## Planned Future Versions

### [1.1.0] - Future
- [ ] Web interface with Flask/FastAPI
- [ ] Support for batch processing
- [ ] Export to JSON/XML
- [ ] OCR results caching
- [ ] Parallel image processing

### [1.2.0] - Future
- [ ] Graphical interface (GUI)
- [ ] Support for other formats (Word, PowerPoint)
- [ ] Alternative OCR backends
- [ ] Visual configuration of regex patterns
- [ ] Statistics dashboard

### [1.3.0] - Future
- [ ] REST API
- [ ] Containerization (Docker)
- [ ] CI/CD pipeline
- [ ] Distribution via PyPI
- [ ] Online documentation 