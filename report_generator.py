from fpdf import FPDF
import datetime

def generate_pdf_report(name, match_score, keywords, filename="Resume_Report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Title
    pdf.set_font("Arial", 'B', size=16)
    pdf.cell(200, 10, txt="AI Resume Match Report", ln=True, align='C')

    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Name: {name}", ln=True)
    pdf.cell(200, 10, txt=f"Date: {datetime.date.today()}", ln=True)
    pdf.ln(10)

    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt=f"Match Score: {match_score}%", ln=True)
    pdf.ln(5)

    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Top Keywords from Job Description:", ln=True)
    pdf.set_font("Arial", size=12)
    for keyword in keywords:
        pdf.cell(200, 10, txt=f"- {keyword}", ln=True)

    pdf.output(filename)
    return filename
