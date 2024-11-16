import re
import csv
import pdfplumber

# Helper function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
        return text

# Helper function to classify PDF type (brochure, letter, or resume)
def classify_pdf(text):
    brochure_keywords = ["brochure"]
    letter_keywords = ["dear", "mr.", "ms.", "sincerely", "regards"]

    text = text.lower()
    if any(keyword in text for keyword in brochure_keywords):
        return "brochure"
    elif any(keyword in text for keyword in letter_keywords):
        return "letter"
    else:
        return "resume"

# Function to extract brochure info
def extract_brochure_info(text):
    lines = text.split('\n')
    
    # Extract company_name, company_address, and company_contact
    company_name = lines[0].strip()  # First line is company name
    company_address = '\n'.join(lines[1:3]).strip()  # Lines 2 and 3 for address
    company_contact = lines[3].strip()  # Line 4 for contact
    
    # Regex to extract product_name, overview, and details (without look-behind)
    product_name = None
    product_overview = None
    product_detail = None
    
    # Searching for product name and other details after certain keywords
    product_name_match = re.search(r'(brochure|overview|details)\s*(.*?)(?=\n\w)', text, re.IGNORECASE)
    if product_name_match:
        product_name = product_name_match.group(2).strip()

    # Extract product_overview after "overview"
    product_overview_match = re.search(r'(?<=\boverview\b)(.*?)(?=\n\bdetailed|details|$)', text, re.DOTALL | re.IGNORECASE)
    if product_overview_match:
        product_overview = product_overview_match.group(0).strip()

    # Extract product_detail after "details"
    product_detail_match = re.search(r'(?<=\bdetails\b)(.*?)(?=\n\boverview|$)', text, re.DOTALL | re.IGNORECASE)
    if product_detail_match:
        product_detail = product_detail_match.group(0).strip()

    # Extract date (month-year)
    date_match = re.search(r'\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+20\d{2}\b', text)
    date = date_match.group(0) if date_match else None

    return {
        "company_name": company_name,
        "company_address": company_address,
        "company_contact": company_contact,
        "date": date,
        "product_name": product_name,
        "product_overview": product_overview,
        "product_detail": product_detail,
    }

# Function to extract letter info
def extract_letter_info(text):
    lines = text.split('\n')
    letter_from = lines[0].strip()  # First line is sender's name
    address = '\n'.join(lines[1:3]).strip()  # Lines 2 and 3 are address
    phone_number = lines[3].strip()  # Line 4 for phone number
    email_address = lines[4].strip()  # Line 5 for email address

    # Regex for recipient's name
    letter_to_match = re.search(r'(?<=\b(Mr\.|Ms\.)\s)(\S.*?),', text)
    letter_to = letter_to_match.group(2).strip() if letter_to_match else None

    # Extract content following the "content" keyword
    content_match = re.search(r'(?<=\bcontent\b)\s*(.*?)(?=\n\bletter|$)', text, re.DOTALL)
    content = content_match.group(0).strip() if content_match else None

    # Extract the date
    date_match = re.search(r'\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+20\d{2}\b', text)
    date = date_match.group(0) if date_match else None

    return {
        "letter_from": letter_from,
        "address": address,
        "phone_number": phone_number,
        "email_address": email_address,
        "date": date,
        "letter_to": letter_to,
        "content": content,
    }

# Function to extract resume info
import re
import csv
import pdfplumber

# Helper function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
        return text

# Helper function to classify PDF type (brochure, letter, or resume)
def classify_pdf(text):
    brochure_keywords = ["brochure"]
    letter_keywords = ["dear", "mr.", "ms.", "sincerely", "regards"]

    text = text.lower()
    if any(keyword in text for keyword in brochure_keywords):
        return "brochure"
    elif any(keyword in text for keyword in letter_keywords):
        return "letter"
    else:
        return "resume"

# Function to extract brochure info
def extract_brochure_info(text):
    # Extract product_name: text before the first occurrence of "brochure"
    product_name = None
    match_product_name = re.search(r"([^\n]+)\s+brochure", text, re.IGNORECASE)
    if match_product_name:
        product_name = match_product_name.group(1).strip()

    # Extract company_name: Typically, the first line of the brochure
    company_name = None
    company_name_match = text.splitlines()[0]
    company_name = company_name_match.strip()

    # Extract company_address: Typically, lines 2 and 3 are the address
    company_address = None
    company_address_lines = text.splitlines()[1:3]  # Address on lines 2 and 3
    company_address = " ".join(company_address_lines).strip()

    # Extract company_contact: Usually, line 4 contains the contact
    company_contact = None
    company_contact_line = text.splitlines()[3]  # Line 4 contains contact
    company_contact = company_contact_line.strip()

    # Extract date: Text that contains month and year (e.g., Jan 2024)
    date = None
    match_date = re.search(r"\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\w*\s+\d{4}\b", text)
    if match_date:
        date = match_date.group(0).strip()

    # Extract product_overview: Look for the section after the "overview" keyword
    product_overview = None
    match_product_overview = re.search(r"overview\s*(.*?)(?=\n|$)", text, re.IGNORECASE)
    if match_product_overview:
        product_overview = match_product_overview.group(1).strip()

    # Extract product_details: Look for the section after the "details" keyword
    product_details = None
    match_product_details = re.search(r"details\s*(.*?)(?=\n|$)", text, re.IGNORECASE)
    if match_product_details:
        product_details = match_product_details.group(1).strip()

    # Return the extracted information as a dictionary
    return {
        "product_name": product_name,
        "company_name": company_name,
        "company_address": company_address,
        "company_contact": company_contact,
        "date": date,
        "product_overview": product_overview,
        "product_details": product_details
    }


# Function to extract letter info
def extract_letter_info(text):
    lines = text.split('\n')
    letter_from = lines[0].strip()  # First line is sender's name
    address = '\n'.join(lines[1:3]).strip()  # Lines 2 and 3 are address
    phone_number = lines[3].strip()  # Line 4 for phone number
    email_address = lines[4].strip()  # Line 5 for email address

    # Regex for recipient's name
    letter_to_match = re.search(r'(?<=\b(Mr\.|Ms\.)\s)(\S.*?),', text)
    letter_to = letter_to_match.group(2).strip() if letter_to_match else None

    # Extract content following the "content" keyword
    content_match = re.search(r'(?<=\bcontent\b)\s*(.*?)(?=\n\bletter|$)', text, re.DOTALL)
    content = content_match.group(0).strip() if content_match else None

    # Extract the date
    date_match = re.search(r'\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+20\d{2}\b', text)
    date = date_match.group(0) if date_match else None

    return {
        "letter_from": letter_from,
        "address": address,
        "phone_number": phone_number,
        "email_address": email_address,
        "date": date,
        "letter_to": letter_to,
        "content": content,
    }

# Function to extract resume info
def extract_resume_info(text):
    # Extract name (flexible pattern)
    name_match = re.search(r"\b(I['’]m|I am)\s+([A-Za-z\s]+)", text)
    name = name_match.group(2).strip() if name_match else None

    # Initialize the variables for address, phone number, and email address
    address = None
    phone_number = None
    email_address = None
    
    if name:
        # Split the text into lines
        lines = text.split('\n')
        # Find the line containing the name to extract subsequent lines
        for i, line in enumerate(lines):
            if name in line:
                # Extract address (next 2 lines after the name)
                address = " ".join(lines[i + 1:i + 3]).strip() if i + 2 < len(lines) else None
                # Extract phone number (the line after the address)
                phone_number = lines[i + 3].strip() if i + 3 < len(lines) else None
                # Extract email address (the line after the phone number)
                email_address = lines[i + 4].strip() if i + 4 < len(lines) else None
                break

    # Extract experience, education, and awards by looking for headings followed by content
    experience = None
    education = None
    awards = None

    # Extract the content for 'experience' by looking for the heading and the following content
    experience_match = re.search(r'(?<=\bexperience\b)[\s\S]*?(?=\n\w)', text, re.IGNORECASE)
    if experience_match:
        experience = experience_match.group(0).strip()

    # Extract the content for 'education' by looking for the heading and the following content
    education_match = re.search(r'(?<=\beducation\b)[\s\S]*?(?=\n\w)', text, re.IGNORECASE)
    if education_match:
        education = education_match.group(0).strip()

    # Extract the content for 'awards' by looking for the heading and the following content
    awards_match = re.search(r'(?<=\bawards\b)[\s\S]*?(?=\n\w)', text, re.IGNORECASE)
    if awards_match:
        awards = awards_match.group(0).strip()

    return {
        "name": name,
        "address": address,
        "phone_number": phone_number,
        "email_address": email_address,
        "experience": experience,
        "education": education,
        "awards": awards,
    }


# Function to write data to CSV file
def write_to_csv(data, filename):
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(data)

# Function to extract and write data to CSV based on PDF type
def extract_and_write_data_from_text(text):
    pdf_type = classify_pdf(text)
    if pdf_type == "brochure":
        data = extract_brochure_info(text)
        write_to_csv(data, 'brochure.csv')
    elif pdf_type == "letter":
        data = extract_letter_info(text)
        write_to_csv(data, 'letter.csv')
    else:
        data = extract_resume_info(text)
        write_to_csv(data, 'resume.csv')



# Function to write data to CSV file
def write_to_csv(data, filename):
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(data)

# Function to extract and write data to CSV based on PDF type
def extract_and_write_data_from_text(text):
    pdf_type = classify_pdf(text)
    if pdf_type == "brochure":
        data = extract_brochure_info(text)
        write_to_csv(data, 'brochure.csv')
    elif pdf_type == "letter":
        data = extract_letter_info(text)
        write_to_csv(data, 'letter.csv')
    else:
        data = extract_resume_info(text)
        write_to_csv(data, 'resume.csv')

