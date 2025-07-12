import pytest
import tempfile
import os
from HireMe.pdf_generator import generate_pdf_resume


def test_generate_pdf_resume():
    """Testa a geração de PDF com currículo e sugestões."""
    # Cria um arquivo temporário de currículo
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt', encoding='utf-8') as temp_resume:
        temp_resume.write("João Silva\nDesenvolvedor Python\nExperiência em automação")
        temp_resume_path = temp_resume.name
    
    # Cria um arquivo temporário para o PDF
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_pdf:
        temp_pdf_path = temp_pdf.name
    
    try:
        suggestions = ["desenvolvimento", "projetos", "tecnologias"]
        
        # Gera o PDF
        generate_pdf_resume(temp_resume_path, suggestions, temp_pdf_path)
        
        # Verifica se o arquivo PDF foi criado
        assert os.path.exists(temp_pdf_path)
        assert os.path.getsize(temp_pdf_path) > 0
        
    finally:
        # Limpa arquivos temporários
        if os.path.exists(temp_resume_path):
            os.unlink(temp_resume_path)
        if os.path.exists(temp_pdf_path):
            os.unlink(temp_pdf_path)


def test_generate_pdf_resume_empty_suggestions():
    """Testa a geração de PDF com lista vazia de sugestões."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt', encoding='utf-8') as temp_resume:
        temp_resume.write("Currículo completo com todas as palavras-chave")
        temp_resume_path = temp_resume.name
    
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_pdf:
        temp_pdf_path = temp_pdf.name
    
    try:
        suggestions = []
        
        # Gera o PDF
        generate_pdf_resume(temp_resume_path, suggestions, temp_pdf_path)
        
        # Verifica se o arquivo PDF foi criado mesmo sem sugestões
        assert os.path.exists(temp_pdf_path)
        assert os.path.getsize(temp_pdf_path) > 0
        
    finally:
        if os.path.exists(temp_resume_path):
            os.unlink(temp_resume_path)
        if os.path.exists(temp_pdf_path):
            os.unlink(temp_pdf_path)


def test_generate_pdf_resume_file_not_found():
    """Testa o comportamento quando o arquivo de currículo não existe."""
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_pdf:
        temp_pdf_path = temp_pdf.name
    
    try:
        suggestions = ["desenvolvimento"]
        
        # Deve gerar uma exceção quando o arquivo não existe
        with pytest.raises(FileNotFoundError):
            generate_pdf_resume("arquivo_inexistente.txt", suggestions, temp_pdf_path)
            
    finally:
        if os.path.exists(temp_pdf_path):
            os.unlink(temp_pdf_path)