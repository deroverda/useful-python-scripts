import os
from fpdf import FPDF

# Function to find the only .txt file in the current directory
def find_txt_file():
    for filename in os.listdir():
        if filename.endswith(".txt"):
            return filename
    return None

# Function to replace unsupported characters with safe alternatives
def sanitize_text(text):
    # Replace special characters with their closest valid equivalents
    replacements = {
        "\u2019": "'",  # Right single quote
        "\u2018": "'",  # Left single quote
        "\u201c": '"',   # Left double quote
        "\u201d": '"',   # Right double quote
        "\u2026": '...', # Ellipsis
        "\u2013": '-',   # En dash
        "\u2014": '--',   # Em dash
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

# Function to convert .txt to .pdf
def convert_txt_to_pdf(txt_file):
    # Create a PDF object
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # Set font (Arial supports basic characters)
    pdf.set_font("Arial", size=10)
    
    # Read the .txt file and add its content to the PDF
    with open(txt_file, "r", encoding="utf-8") as file:
        for line in file:
            sanitized_line = sanitize_text(line)
            # Remove any unnecessary leading/trailing whitespace from lines
            sanitized_line = sanitized_line.strip()
            # Adjust line height to reduce spacing
            pdf.multi_cell(0, 8, sanitized_line, align='L')  # Line height set to 8
    
    # Output the PDF to a file with the same name as the .txt file
    pdf_file = os.path.splitext(txt_file)[0] + ".pdf"
    pdf.output(pdf_file)
    print(f"PDF saved as: {pdf_file}")

# Main code
txt_file = find_txt_file()
if txt_file:
    convert_txt_to_pdf(txt_file)
else:
    print("No .txt file found in the current directory.")
