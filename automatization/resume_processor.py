def analyze_resume(base_resume, keywords):
    """
    Analisa o currículo e retorna palavras-chave ausentes.

    Args:
        base_resume (str): Caminho para o arquivo do currículo base.
        keywords (list[str]): Lista de palavras-chave para verificar.

    Returns:
        list[str]: Palavras-chave ausentes no currículo.
    """
    try:
        with open(base_resume, "r", encoding="utf-8") as file:
            resume_text = file.read().lower()

        # Identifica palavras-chave ausentes
        missing_keywords = [word for word in keywords if word.lower() not in resume_text]
        return missing_keywords
    except FileNotFoundError:
        raise FileNotFoundError(f"O arquivo {base_resume} não foi encontrado.")
    except Exception as e:
        raise RuntimeError(f"Erro ao analisar o currículo: {e}")