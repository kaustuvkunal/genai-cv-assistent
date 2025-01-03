from pypdf import PdfReader
import streamlit as st

def read_pdf(pdf_doc):
    """Extract text from a PDF document."""
    try:
        pdf = PdfReader(pdf_doc)
        raw_text = ""
        for page in pdf.pages:
            content = page.extract_text()
            if content:
                raw_text += content
        if not raw_text.strip():
            raise ValueError("PDF does not contain readable text.")
        return raw_text
    except Exception as e:
        st.error(f"Error reading PDF: {str(e)}")
        return ""