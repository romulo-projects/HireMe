import pytest
import tempfile
import os
from HireMe.pdf_generator import generate_pdf_resume, PDFResume


def test_pdf_resume_header():
    """
    Testa se a classe PDFResume adiciona cabeçalho corretamente.
    """
    pdf = PDFResume()
    pdf.add_page()
    
    # Verifica se o PDF foi criado
    assert pdf.page_no() == 1


def test_generate_pdf_resume():
    """
    Testa a geração de PDF com currículo base e sugestões.
    """
    # Cria arquivo temporário de currículo
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as resume_file:
        resume_file.write("João Silva\nDesenvolvedor Python\nExperiência em automação.")
        resume_path = resume_file.name
    
    # Cria arquivo temporário para o PDF de saída
    with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as pdf_file:
        pdf_path = pdf_file.name
    
    try:
        suggestions = ["machine learning", "desenvolvimento web"]
        
        # Gera o PDF
        generate_pdf_resume(resume_path, suggestions, pdf_path)
        
        # Verifica se o arquivo PDF foi criado
        assert os.path.exists(pdf_path)
        assert os.path.getsize(pdf_path) > 0
        
    finally:
        # Limpa arquivos temporários
        if os.path.exists(resume_path):
            os.unlink(resume_path)
        if os.path.exists(pdf_path):
            os.unlink(pdf_path)


def test_generate_pdf_resume_empty_suggestions():
    """
    Testa a geração de PDF com lista vazia de sugestões.
    """
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as resume_file:
        resume_file.write("João Silva\nDesenvolvedor Python completo.")
        resume_path = resume_file.name
    
    with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as pdf_file:
        pdf_path = pdf_file.name
    
    try:
        suggestions = []
        
        generate_pdf_resume(resume_path, suggestions, pdf_path)
        
        assert os.path.exists(pdf_path)
        assert os.path.getsize(pdf_path) > 0
        
    finally:
        if os.path.exists(resume_path):
            os.unlink(resume_path)
        if os.path.exists(pdf_path):
            os.unlink(pdf_path)