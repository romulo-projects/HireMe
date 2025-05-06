import pytest
from automatizador_curriculos.resume_processor import analyze_resume

def test_analyze_resume_keywords_present():
    resume_content = "Python e automação são habilidades importantes."
    keywords = ["python", "automação"]
    with open("test_curriculo.txt", "w") as f:
        f.write(resume_content)
    
    missing_keywords = analyze_resume("test_curriculo.txt", keywords)
    assert missing_keywords == []

def test_analyze_resume_keywords_missing():
    resume_content = "Python e automação são habilidades importantes."
    keywords = ["python", "desenvolvimento"]
    with open("test_curriculo.txt", "w") as f:
        f.write(resume_content)
    
    missing_keywords = analyze_resume("test_curriculo.txt", keywords)
    assert missing_keywords == ["desenvolvimento"]