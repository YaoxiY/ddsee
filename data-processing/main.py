from pdf_extractor import extract_and_write_data_from_text
from pdf_parser import extract_text_from_pdf
import os

def main():
    # Path to the folder containing PDFs
    pdf_folder_path = r'C:\Download\PortableGit\ddsee\data-processing\pdfs'
    
    # Verify the folder exists
    if not os.path.isdir(pdf_folder_path):
        print(f"Folder not found: {pdf_folder_path}")
        return

    # Process each PDF in the folder
    for filename in os.listdir(pdf_folder_path):
        if filename.endswith(".pdf"):  # Ensure it's a PDF file
            pdf_path = os.path.join(pdf_folder_path, filename)
            print(f"Processing: {pdf_path}")
            
            # Extract text from the PDF
            text = extract_text_from_pdf(pdf_path)
            
            # Classify and write data
            extract_and_write_data_from_text(text)

if __name__ == "__main__":
    main()
