import unittest
from src.pdf_parser import extract_text_from_pdf

class TestPDFParser(unittest.TestCase):
    def test_extract_text_from_pdf(self):
        pdf_path = 'pdfs/sample-1.pdf'
        text = extract_text_from_pdf(pdf_path)
        self.assertIsNotNone(text)
        self.assertIsInstance(text, str)

if __name__ == '__main__':
    unittest.main()