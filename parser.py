import pdfplumber
from docx import Document


def extract_text(file):

    text = ""

    if file.endswith(".pdf"):

        with pdfplumber.open(file) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

    elif file.endswith(".docx"):

        doc = Document(file)

        for para in doc.paragraphs:
            text += para.text + "\n"

    return text