import pytest
import tempfile
import os
from HireMe.resume_processor import analyze_resume


def test_analyze_resume_missing_keywords():
    """Testa a identificação de palavras-chave ausentes no currículo."""
    # Cria um arquivo temporário para teste
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt', encoding='utf-8') as temp_file:
        temp_file.write("João Silva\nDesenvolvedor Python\nExperiência em automação")
        temp_file_path = temp_file.name
    
    try:
        keywords = ["python", "automação", "desenvolvimento", "projetos"]
        missing = analyze_resume(temp_file_path, keywords)
        
        # Deve encontrar "desenvolvimento" e "projetos" como ausentes
        assert "desenvolvimento" in missing
        assert "projetos" in missing
        assert "python" not in missing
        assert "automação" not in missing
    finally:
        os.unlink(temp_file_path)


def test_analyze_resume_no_missing_keywords():
    """Testa quando todas as palavras-chave estão presentes."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt', encoding='utf-8') as temp_file:
        temp_file.write("Desenvolvedor Python com experiência em automação e desenvolvimento de projetos")
        temp_file_path = temp_file.name
    
    try:
        keywords = ["python", "automação", "desenvolvimento", "projetos"]
        missing = analyze_resume(temp_file_path, keywords)
        
        assert len(missing) == 0
    finally:
        os.unlink(temp_file_path)


def test_analyze_resume_file_not_found():
    """Testa o comportamento quando o arquivo não existe."""
    with pytest.raises(FileNotFoundError):
        analyze_resume("arquivo_inexistente.txt", ["python"])


def test_analyze_resume_case_insensitive():
    """Testa se a busca é case-insensitive."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt', encoding='utf-8') as temp_file:
        temp_file.write("PYTHON DESENVOLVIMENTO automação")
        temp_file_path = temp_file.name
    
    try:
        keywords = ["python", "desenvolvimento", "automação", "projetos"]
        missing = analyze_resume(temp_file_path, keywords)
        
        # Apenas "projetos" deve estar ausente
        assert missing == ["projetos"]
    finally:
        os.unlink(temp_file_path)