import PyPDF2
import os

def extract_text_from_pdf(pdf_dir):
    try:
        # Check if the provided directory exists
        if not os.path.isdir(pdf_dir):
            print("Error: The provided path is not a valid directory.")
            return

        # Find the first PDF file in the directory
        pdf_files = [f for f in os.listdir(pdf_dir) if f.lower().endswith('.pdf')]
        
        if not pdf_files:
            print("Error: No PDF file found in the specified directory.")
            return

        # Take the first PDF file found (if multiple PDFs are found, you can adjust this part)
        pdf_path = os.path.join(pdf_dir, pdf_files[0])

        # Define the output text file path in the same directory
        output_text_file = os.path.join(pdf_dir, 'extracted_text.txt')

        # Open the PDF file in read-binary mode
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            extracted_text = ""

            # Loop through each page and extract text
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                extracted_text += page.extract_text()

            # Save extracted text to the output file with UTF-8 encoding
            with open(output_text_file, 'w', encoding='utf-8') as output_file:
                output_file.write(extracted_text)

            print(f"Text successfully extracted from {pdf_path} and saved to {output_text_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage: User chooses the directory containing the PDF
pdf_dir = input("Enter the path to the directory containing the PDF file: ")
extract_text_from_pdf(pdf_dir)
