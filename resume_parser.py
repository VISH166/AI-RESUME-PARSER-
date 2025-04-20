import pdfplumber
import docx2txt
import io

def extract_text(file):
    # For PDF files
    if file.name.endswith('.pdf'):
        text = ""
        with pdfplumber.open(io.BytesIO(file.read())) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text

    # For DOCX files
    elif file.name.endswith('.docx'):
        # Save the uploaded file temporarily
        with open("temp_resume.docx", "wb") as f:
            f.write(file.read())
        return docx2txt.process("temp_resume.docx")

    # Unsupported file type
    else:
        return "Unsupported file type"

