from pypdf import PdfReader
import logging


# Updated PDF parsing with logging
def read_pdf(pdf_doc):
    logging.info("Starting PDF reading process.")
    try:
        pdf = PdfReader(pdf_doc)
        raw_text = ''
        for i, page in enumerate(pdf.pages):
            content = page.extract_text()
            if content:
                raw_text += content
        logging.info("PDF reading completed successfully.")
        return raw_text
    except Exception as e:
        logging.error(f"Error reading PDF: {e}")
        raise