# OCR PDF Reader - Makefile

.PHONY: help install test lint clean run example

# Configurações
PYTHON = python
UV = uv

help:  ## Mostra esta ajuda
	@echo "OCR PDF Reader - Comandos disponíveis:"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install:  ## Instala as dependências do projeto
	$(UV) sync

install-dev:  ## Instala dependências de desenvolvimento
	$(UV) sync --extra dev

test:  ## Executa os testes unitários
	$(UV) run $(PYTHON) -m pytest tests/ -v

test-coverage:  ## Executa testes com cobertura
	$(UV) run $(PYTHON) -m pytest tests/ --cov=src/ocr_pdf_reader --cov-report=html

lint:  ## Executa verificações de código
	$(UV) run black --check src/ tests/
	$(UV) run flake8 src/ tests/
	$(UV) run mypy src/

format:  ## Formata o código
	$(UV) run black src/ tests/
	$(UV) run isort src/ tests/

clean:  ## Remove arquivos temporários
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -name "*.pyc" -delete
	rm -rf dist/ build/ .coverage htmlcov/ logs/ temp/

run:  ## Executa o programa em modo interativo
	$(UV) run $(PYTHON) -m ocr_pdf_reader

run-help:  ## Mostra a ajuda do programa
	$(UV) run $(PYTHON) -m ocr_pdf_reader --help

build:  ## Constrói o pacote
	$(UV) build

example:  ## Executa o exemplo programático
	$(UV) run $(PYTHON) examples/example.py

test-integration:  ## Executa testes de integração
	$(UV) run $(PYTHON) tests/test_real_format.py
	$(UV) run $(PYTHON) tests/test_line_breaking.py
	$(UV) run $(PYTHON) tests/test_remove_ending.py

check:  ## Executa todas as verificações
	make lint
	make test

dev-setup:  ## Configura ambiente de desenvolvimento
	make install-dev
	$(UV) run pre-commit install

# Comandos de uso direto
extract:  ## Extrai texto de um PDF (uso: make extract PDF=arquivo.pdf)
	$(UV) run $(PYTHON) -m ocr_pdf_reader $(PDF)

extract-to:  ## Extrai para arquivo específico (uso: make extract-to PDF=arquivo.pdf OUT=resultado.txt)
	$(UV) run $(PYTHON) -m ocr_pdf_reader $(PDF) -o $(OUT) 