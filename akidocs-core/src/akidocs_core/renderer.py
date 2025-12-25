from fpdf import FPDF

from akidocs_core.tokens import Header, Paragraph


def render_pdf(tokens: list) -> bytes:
    pdf = FPDF()
    pdf.add_page()

    for token in tokens:
        if isinstance(token, Header):
            level = token.level
            size = {1: 24, 2: 20, 3: 16, 4: 14, 5: 12, 6: 11}.get(level, 12)
            pdf.set_font("Times", style="B", size=size)
            pdf.multi_cell(0, size * 0.5, token.content)
            pdf.ln(4)
        elif isinstance(token, Header):
            pdf.set_font("Times", size=12)
            pdf.multi_cell(0, 6, token.content)
            pdf.ln(2)

    return bytes(pdf.output())
