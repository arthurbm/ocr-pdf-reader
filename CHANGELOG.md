# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
e este projeto segue [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-12-31

### 🎉 Primeira Release Estável

### Added
- ✨ **Arquitetura modular completa**
  - Separação em módulos especializados (`core`, `image_processor`, `text_processor`, `cli`)
  - Estrutura de pacote Python profissional
  - Configurações centralizadas

- 🚀 **Múltiplas interfaces de uso**
  - Interface de linha de comando (CLI) com argumentos
  - Modo interativo para usuários iniciantes  
  - API programática para desenvolvedores
  - Script de compatibilidade (`main.py`)

- 🧠 **Processamento inteligente de texto**
  - Detecção automática de códigos no formato "XX.XX.XX - DESCRIÇÃO"
  - Manutenção de siglas organizacionais (ex: "- GR", "- CCsA")
  - Tratamento de linhas quebradas pelo OCR
  - Validação e limpeza automática de texto

- 📦 **Gerenciamento de dependências moderno**
  - Configuração com `pyproject.toml`
  - Suporte completo ao UV (Python package manager)
  - Dependências versionadas e compatíveis

- 🧪 **Testes e qualidade**
  - Testes unitários para funcionalidades críticas
  - Estrutura de testes organizada
  - Configuração para ferramentas de qualidade (Black, Flake8, MyPy)

- 📚 **Documentação completa**
  - README detalhado com exemplos
  - Documentação de arquitetura (ARCHITECTURE.md)
  - Exemplos de uso programático
  - Makefile com comandos úteis

- ⚙️ **Configurações flexíveis**
  - Padrões regex configuráveis para diferentes formatos
  - Parâmetros de OCR ajustáveis
  - Suporte a múltiplos idiomas
  - Sistema de logging configurável

### Core Features
- 🔍 **Extração de imagens de PDFs** usando PyMuPDF
- 👁️ **OCR com Tesseract** e pré-processamento de imagens
- 📝 **Processamento inteligente** de texto extraído
- 🎯 **Resultado limpo** sem códigos numéricos, mantendo apenas descrições
- 🔧 **Compatibilidade** mantida com versão anterior

### Technical Improvements
- Type hints em todas as funções
- Docstrings completas
- Tratamento robusto de erros
- Logging estruturado
- Código seguindo PEP 8
- Arquitetura extensível

### Supported Formats
- PDFs com imagens incorporadas
- PDFs renderizados como imagem
- Formatos de código: "X - TEXTO", "XX.XX - TEXTO", "XX.XX.XX - TEXTO"
- Texto corrido e linhas quebradas

### Requirements
- Python 3.9+
- Tesseract OCR instalado no sistema
- Dependências: PyMuPDF, pytesseract, Pillow, opencv-python

## [0.1.0] - 2024-12-30

### Initial Development
- 🚀 **Primeira versão funcional**
- ✅ Extração básica de texto de PDFs
- ✅ Processamento simples de linhas numeradas
- ✅ Script monolítico em `main.py`

---

## Próximas Versões Planejadas

### [1.1.0] - Futuro
- [ ] Interface web com Flask/FastAPI
- [ ] Suporte a batch processing
- [ ] Export para JSON/XML
- [ ] Cache de resultados OCR
- [ ] Processamento paralelo de imagens

### [1.2.0] - Futuro
- [ ] Interface gráfica (GUI)
- [ ] Suporte a outros formatos (Word, PowerPoint)
- [ ] OCR backends alternativos
- [ ] Configuração visual de regex patterns
- [ ] Dashboard de estatísticas

### [1.3.0] - Futuro
- [ ] API REST
- [ ] Containerização (Docker)
- [ ] CI/CD pipeline
- [ ] Distribuição via PyPI
- [ ] Documentação online 