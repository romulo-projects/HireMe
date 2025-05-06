# HireMe

**HireMe** é uma ferramenta poderosa para análise e melhoria de currículos. Com uma interface gráfica simples e intuitiva, ela permite que usuários processem currículos, identifiquem palavras-chave ausentes e gerem PDFs personalizados com sugestões de melhorias.

---

## 📋 Funcionalidades

- **Análise de currículos**: Identifica palavras-chave ausentes que podem melhorar o impacto do currículo.
- **Geração de PDFs personalizados**: Inclui o conteúdo do currículo base e as sugestões de melhorias.
- **Interface gráfica amigável**: Desenvolvida com `tkinter` para facilitar a interação do usuário.
- **Suporte a arquivos de texto (`.txt`)**: Ideal para currículos simples.

---

## 🚀 Como Usar

### 1. Pré-requisitos
Certifique-se de que você tem o Python 3.10 ou superior instalado. Instale as dependências necessárias com o seguinte comando:
```bash
pip install -r requirements.txt
```

### 2. Executando o Programa
1. Navegue até o diretório do projeto:
   ```bash
   cd HireMe
   ```
2. Execute o arquivo principal:
   ```bash
   python main.py
   ```
3. Siga as instruções na interface gráfica:
   - **Selecione um currículo base**: Escolha um arquivo `.txt` com o conteúdo do seu currículo.
   - **Processar currículo**: Analise o currículo e gere sugestões de melhorias.
   - **Salvar o PDF**: Escolha um local para salvar o PDF gerado.

---

## 📂 Estrutura do Projeto

```plaintext
HireMe/
├── automatization/                # Código principal do projeto
│   ├── __init__.py                # Inicializador do pacote
│   ├── gui.py                     # Interface gráfica
│   ├── pdf_generator.py           # Geração de PDFs
│   └── resume_processor.py        # Processamento e análise de currículos
├── curriculos_base/               # Diretório para currículos de teste
│   └── curriculo_base.txt         # Exemplo de currículo base
├── tests/                         # Testes automatizados
│   └── tests_resume_processor.py  # Testes para o módulo de processamento
├── main.py                        # Ponto de entrada principal
├── requirements.txt               # Dependências do projeto
├── README.md                      # Documentação do projeto
└── __pycache__/                   # Cache de compilação do Python
```

---

## 🧪 Testes

Os testes automatizados estão localizados no diretório `tests/`. Para executá-los, use o `pytest`:
```bash
pytest tests/
```

Exemplo de um teste para o módulo `resume_processor.py`:
```python
def test_analyze_resume():
    resume_text = "Python e automação são habilidades importantes."
    keywords = ["python", "automação", "desenvolvimento"]
    missing = analyze_resume("exemplo_curriculo.txt", keywords)
    assert missing == ["desenvolvimento"]
```

---

## 🎨 Exemplo de Resultado

Após processar um currículo, você receberá um PDF com o conteúdo do currículo base e as sugestões de palavras-chave ausentes. Aqui está um exemplo de como será o PDF:

- **Currículo Base**:
  ```
  João Silva
  Desenvolvedor de Software
  Email: joao.silva@email.com

  Experiência:
  - Desenvolvimento de aplicações web em Python e Django.
  - Criação de scripts de automação.
  ```

- **Sugestões de Melhorias**:
  ```
  --- Sugestões de Melhorias ---
  - Incluir: desenvolvimento
  - Incluir: automação
  ```

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10**: Linguagem principal do projeto.
- **tkinter**: Para a interface gráfica.
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