# OCR PDF Reader - Makefile

.PHONY: help install test lint clean run example

# Settings
PYTHON = python
UV = uv

help:  ## Show this help
	@echo "OCR PDF Reader - Available commands:"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install:  ## Install project dependencies
	$(UV) sync

install-dev:  ## Install development dependencies
	$(UV) sync --extra dev

test:  ## Run unit tests
	$(UV) run $(PYTHON) -m pytest tests/ -v

test-coverage:  ## Run tests with coverage
	$(UV) run $(PYTHON) -m pytest tests/ --cov=src/ocr_pdf_reader --cov-report=html

lint:  ## Run code checks
	$(UV) run black --check src/ tests/
	$(UV) run flake8 src/ tests/
	$(UV) run mypy src/

format:  ## Format code
	$(UV) run black src/ tests/
	$(UV) run isort src/ tests/

clean:  ## Remove temporary files
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -name "*.pyc" -delete
	rm -rf dist/ build/ .coverage htmlcov/ logs/ temp/

run:  ## Run the program in interactive mode
	$(UV) run $(PYTHON) -m ocr_pdf_reader

run-help:  ## Show program help
	$(UV) run $(PYTHON) -m ocr_pdf_reader --help

build:  ## Build the package
	$(UV) build

example:  ## Run programmatic example
	$(UV) run $(PYTHON) examples/example.py

test-integration:  ## Run integration tests
	$(UV) run $(PYTHON) tests/test_real_format.py
	$(UV) run $(PYTHON) tests/test_line_breaking.py
	$(UV) run $(PYTHON) tests/test_remove_ending.py

check:  ## Run all checks
	make lint
	make test

dev-setup:  ## Setup development environment
	make install-dev
	$(UV) run pre-commit install

# Direct usage commands
extract:  ## Extract text from PDF (usage: make extract PDF=file.pdf)
	$(UV) run $(PYTHON) -m ocr_pdf_reader $(PDF)

extract-to:  ## Extract to specific file (usage: make extract-to PDF=file.pdf OUT=result.txt)
	$(UV) run $(PYTHON) -m ocr_pdf_reader $(PDF) -o $(OUT) 