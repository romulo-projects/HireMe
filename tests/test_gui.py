import sys
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox
from HireMe.resume_processor import analyze_resume
from HireMe.pdf_generator import generate_pdf_resume


# Adiciona o caminho do projeto ao sys.path (se necessário)
PROJECT_PATH = Path(__file__).parent.parent
sys.path.append(str(PROJECT_PATH))

def select_resume_file():
    """
    Abre um diálogo para o usuário selecionar o arquivo do currículo base.
    """
    file_path = filedialog.askopenfilename(
        filetypes=[("Arquivos de texto", "*.txt")],
        title="Selecione o arquivo do currículo base"
    )
    if file_path:
        resume_file_path.set(file_path)

def process_resume():
    """
    Analisa o currículo selecionado, verifica palavras-chave ausentes e gera um PDF com sugestões de melhorias.
    """
    resume_path = resume_file_path.get()
    if not resume_path:
        messagebox.showerror("Erro", "Por favor, selecione um arquivo de currículo.")
        return

    try:
        # Lista de palavras-chave que podem ser ajustadas conforme a necessidade
        keywords = ["python", "desenvolvimento", "automação", "projetos", "tecnologias"]
        missing_keywords = analyze_resume(resume_path, keywords)

        if missing_keywords:
            output_file = filedialog.asksaveasfilename(
                defaultextension=".pdf",
                filetypes=[("Arquivos PDF", "*.pdf")],
                title="Salvar currículo gerado"
            )
            if output_file:
                generate_pdf_resume(resume_path, missing_keywords, output_file)
                messagebox.showinfo("Sucesso", "Currículo processado e salvo com sucesso!")
        else:
            messagebox.showinfo("Informação", "Nenhuma sugestão necessária. Seu currículo já está completo!")
    except FileNotFoundError:
        messagebox.showerror("Erro", "O arquivo do currículo não foi encontrado.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao processar o currículo: {e}")

def setup_ui():
    """
    Configura a interface gráfica do programa.
    """
    global resume_file_path  # Torna a variável disponível para outras funções
    root = tk.Tk()
    root.title("HireMe - Automatizador de Currículos")
    root.geometry("400x200")
    root.resizable(False, False)

    # Inicializa a variável depois de criar o root
    resume_file_path = tk.StringVar()

    tk.Label(root, text="HireMe - Automatizador de Currículos", font=("Arial", 16, "bold")).pack(pady=10)
    tk.Button(root, text="Selecionar Currículo Base", command=select_resume_file, width=30).pack(pady=5)
    tk.Button(root, text="Processar Currículo", command=process_resume, width=30).pack(pady=5)
    tk.Entry(root, textvariable=resume_file_path, state="readonly", width=50).pack(pady=10)

    tk.Label(root, text="Selecione um arquivo .txt e processe seu currículo.", font=("Arial", 10, "italic")).pack(pady=10)
    return root

# Inicializa a interface
if __name__ == "__main__":
    app = setup_ui()
    app.mainloop()