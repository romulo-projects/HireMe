import pytest
import tempfile
import os
from HireMe.resume_processor import analyze_resume


def test_analyze_resume_missing_keywords():
    """
    Testa se a função identifica corretamente palavras-chave ausentes.
    """
    # Cria um arquivo temporário com conteúdo de teste
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as tmp_file:
        tmp_file.write("João Silva\nDesenvolvedor Python\nExperiência em automação de testes.")
        tmp_file_path = tmp_file.name
    
    try:
        keywords = ["python", "automação", "desenvolvimento", "machine learning"]
        missing = analyze_resume(tmp_file_path, keywords)
        
        # Deve encontrar "machine learning" e "desenvolvimento" como ausentes
        assert "machine learning" in missing
        assert "desenvolvimento" in missing
        assert "python" not in missing
        assert "automação" not in missing
        
    finally:
        # Limpa o arquivo temporário
        os.unlink(tmp_file_path)


def test_analyze_resume_no_missing_keywords():
    """
    Testa quando não há palavras-chave ausentes.
    """
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as tmp_file:
        tmp_file.write("Desenvolvedor Python com experiência em automação e projetos.")
        tmp_file_path = tmp_file.name
    
    try:
        keywords = ["python", "automação", "projetos"]
        missing = analyze_resume(tmp_file_path, keywords)
        
        assert missing == []
        
    finally:
        os.unlink(tmp_file_path)


def test_analyze_resume_file_not_found():
    """
    Testa se a função levanta exceção quando o arquivo não existe.
    """
    with pytest.raises(FileNotFoundError):
        analyze_resume("arquivo_inexistente.txt", ["python"])