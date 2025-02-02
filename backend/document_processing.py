import fitz  # PyMuPDF for PDF handling
import docx
import os

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    doc = fitz.open(pdf_path)
    text = "\n".join([page.get_text() for page in doc])
    return text

def extract_text_from_docx(docx_path):
    """Extract text from a DOCX file."""
    doc = docx.Document(docx_path)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text(file_path):
    """Extract text based on file type."""
    _, ext = os.path.splitext(file_path)
    
    if ext.lower() == ".pdf":
        return extract_text_from_pdf(file_path)
    elif ext.lower() in [".doc", ".docx"]:
        return extract_text_from_docx(file_path)
    elif ext.lower() == ".txt":
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    else:
        raise ValueError("Unsupported file type. Please upload a PDF, DOCX, or TXT file.")
