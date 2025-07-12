# HireMe

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)](#testes)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**HireMe** é uma ferramenta poderosa para análise e melhoria de currículos. Com uma interface gráfica simples e intuitiva, ela permite que usuários processem currículos, identifiquem palavras-chave ausentes e gerem PDFs personalizados com sugestões de melhorias.

---

## 📋 Funcionalidades

- **Análise de currículos**: Identifica palavras-chave ausentes que podem melhorar o impacto do currículo.
- **Geração de PDFs personalizados**: Inclui o conteúdo do currículo base e as sugestões de melhorias.
- **Interface gráfica amigável**: Desenvolvida com `tkinter` e `ttkbootstrap` para facilitar a interação do usuário.
- **Suporte a arquivos de texto (`.txt`)**: Ideal para currículos simples.
- **Mensagens de feedback**: A interface informa sobre sucesso, erros de arquivo e se o currículo já está completo.

---

## 🚀 Como Usar

### 1. Pré-requisitos
Certifique-se de que você tem o Python 3.10 ou superior instalado.

### 2. Instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/romulo-projects/HireMe.git
   cd HireMe
   ```
2. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```

### 3. Executando o Programa
1. Execute o arquivo principal:
   ```bash
   python main.py
   ```
2. Siga as instruções na interface gráfica:
   - **Selecione um currículo base**: Escolha um arquivo `.txt` com o conteúdo do seu currículo (há exemplos em `modelos_curriculos/`).
   - **Processar currículo**: Analise o currículo e gere sugestões de melhorias.
   - **Salvar o PDF**: Escolha um local para salvar o PDF gerado.

---

## ℹ️ Observações adicionais

- **Palavras-chave padrão:** As palavras-chave analisadas por padrão são: `python`, `desenvolvimento`, `automação`, `projetos`, `tecnologias`. Para personalizar, edite a lista no arquivo `HireMe/gui.py`.
- **Modelos de currículo:** Exemplos para teste estão disponíveis na pasta `modelos_curriculos/`.
- **Mensagens na interface:** O usuário será informado caso o currículo já esteja completo, se ocorrer erro de arquivo, ou ao salvar o PDF com sucesso.
- **Formatos suportados:** Apenas arquivos `.txt` são aceitos no momento. Suporte a outros formatos está planejado (ver "Próximos Passos").

---

## 📂 Estrutura do Projeto

```plaintext
HireMe/
├── HireMe/                          # Código principal do projeto
│   ├── __init__.py                  # Inicializador do pacote
│   ├── gui.py                       # Interface gráfica
│   ├── pdf_generator.py             # Geração de PDFs
│   └── resume_processor.py          # Processamento e análise de currículos
├── modelos_curriculos/              # Diretório para modelos de currículos
│   └── modelo_curriculo.txt         # Exemplo de modelo de currículo
├── tests/                           # Testes automatizados
│   ├── test_resume_processor.py     # Testes para o módulo de processamento
│   ├── test_pdf_generator.py        # Testes para o gerador de PDF
│   └── test_gui.py                  # Testes para a interface gráfica
├── main.py                          # Ponto de entrada principal
├── requirements.txt                 # Dependências do projeto
├── README.md                        # Documentação do projeto
├── LICENSE                          # Licença do projeto (MIT)
└── .gitignore                       # Arquivos ignorados pelo Git
```

---

## 🧪 Testes

Os testes automatizados estão localizados no diretório `tests/`. Para executá-los, use o `pytest`:
```bash
pytest tests/
```

Para executar os testes com cobertura de código:
```bash
pytest tests/ --cov=HireMe --cov-report=html
```

Há testes para o processamento de currículos, geração de PDF e interface gráfica.

Exemplo de um teste para o módulo `resume_processor.py`:
```python
def test_analyze_resume_missing_keywords():
    # Cria um arquivo temporário com conteúdo de teste
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as tmp_file:
        tmp_file.write("João Silva\nDesenvolvedor Python\nExperiência em automação de testes.")
        tmp_file_path = tmp_file.name
    
    keywords = ["python", "automação", "desenvolvimento", "machine learning"]
    missing = analyze_resume(tmp_file_path, keywords)
    
    assert "machine learning" in missing
    assert "desenvolvimento" in missing
```

## 👨‍💻 Desenvolvimento

### Configuração do Ambiente de Desenvolvimento
1. Clone o repositório
2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```
3. Instale as dependências de desenvolvimento:
   ```bash
   pip install -r requirements.txt
   ```

### Ferramentas de Desenvolvimento
- **Formatação de código**: `black`
- **Linting**: `flake8`
- **Verificação de tipos**: `mypy`
- **Testes**: `pytest`

Para formatar o código:
```bash
black HireMe/ tests/
```

Para verificar o estilo do código:
```bash
flake8 HireMe/ tests/
```

---

## 🎨 Exemplo de Resultado

Após processar um currículo, você receberá um PDF com o conteúdo do currículo base e as sugestões de palavras-chave ausentes. Aqui está um exemplo de como será o PDF:

- **Currículo Base:**
  ```
  João Silva
  Desenvolvedor de Software
  Email: joao.silva@email.com

  Experiência:
  - Desenvolvimento de aplicações web em Python e Django.
  - Criação de scripts de automação.
  ```

- **Sugestões de Melhorias:**
  ```
  --- Sugestões de Melhorias ---
  - Incluir: desenvolvimento
  - Incluir: automação
  ```

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10**: Linguagem principal do projeto.
- **tkinter**: Para a interface gráfica.
- **ttkbootstrap**: Para temas modernos na interface gráfica.
- **FPDF**: Para gerar PDFs.
- **pytest**: Para testes automatizados.

---

## 📌 Próximos Passos

- Suporte a arquivos `.docx` (Word).
- Adicionar barra de progresso na interface gráfica.
- Melhorar a formatação dos PDFs (cores, cabeçalhos, etc.).
- Adicionar configuração para personalizar palavras-chave.

---

## 📜 Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [`LICENSE`](LICENSE) para mais detalhes.

---

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir **issues** ou enviar **pull requests**.

---

## 📧 Contato

Se tiver dúvidas ou sugestões, entre em contato:
- **Autor**: Romulo Gomes Della Libera
- **Email**: romulo.libera@gmail.com
