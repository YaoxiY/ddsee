import pdfplumber

def extract_text_from_pdf(pdf_path):
    """
    Extracts all text from a PDF file.
    :param pdf_path: Path to the PDF file
    :return: Extracted text as a string
    """
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ''
            for page in pdf.pages:
                text += page.extract_text() or ''  # Handle empty pages gracefully
            return text
    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")
        return ""
