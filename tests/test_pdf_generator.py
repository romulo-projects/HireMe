from fpdf import FPDF


class PDFResume(FPDF):
    """
    Classe personalizada para geração de PDFs de currículos.
    """
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Currículo Gerado - HireMe", align="C", ln=True)
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Página {self.page_no()}", align="C")


def generate_pdf_resume(base_resume, suggestions, output_file):
    """
    Gera um PDF com o conteúdo do currículo base e sugestões de melhorias.

    Args:
        base_resume (str): Caminho para o arquivo do currículo base.
        suggestions (list): Lista de sugestões de palavras-chave.
        output_file (str): Caminho para salvar o arquivo PDF gerado.
    """
    pdf = PDFResume()
    pdf.add_page()

    # Adiciona o currículo base
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, "Currículo Base", ln=True, align="L")
    pdf.ln(5)

    with open(base_resume, "r", encoding="utf-8") as file:
        for line in file:
            pdf.multi_cell(0, 10, txt=line.strip())

    # Adiciona sugestões de melhoria
    pdf.ln(10)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Sugestões de Melhorias", ln=True, align="L")
    pdf.set_font("Arial", size=12)

    for suggestion in suggestions:
        pdf.cell(0, 10, f"- Incluir: {suggestion}", ln=True)

    # Salva o arquivo PDF
    pdf.output(output_file, "F")