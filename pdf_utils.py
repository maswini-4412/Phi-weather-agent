from fpdf import FPDF

def generate_pdf(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 8, text)

    file_path = "weather_report.pdf"
    pdf.output(file_path)
    return file_path 