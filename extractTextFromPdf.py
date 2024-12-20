import os

from PIL import Image
import logging
import pytesseract # type: ignore
from pdf2image import convert_from_path # type: ignore

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Path to the PDF file
pdf_path = 'path/to/your/pdf_file.pdf'
# Path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'path/to/tesseract.exe'

# Check if the PDF file exists
if not os.path.exists(pdf_path):
    logging.error(f"PDF file not found: {pdf_path}")
    raise FileNotFoundError(f"PDF file not found: {pdf_path}")

try:
    # Convert PDF to images
    logging.info(f"Converting PDF to images: {pdf_path}")
    pages = convert_from_path(pdf_path, 300)
except Exception as e:
    logging.error(f"Error converting PDF to images: {e}")
    raise

# Extract text from each image
extracted_text = ""
for page_number, page_data in enumerate(pages):
    try:
        logging.info(f"Extracting text from page {page_number + 1}")
        text = pytesseract.image_to_string(page_data)
        extracted_text += f"Page {page_number + 1}:\n{text}\n\n"
    except Exception as e:
        logging.error(f"Error extracting text from page {page_number + 1}: {e}")
        continue

# Save the extracted text to a file
output_file = 'extracted_text.txt'
try:
    with open(output_file, 'w', encoding='utf-8') as text_file:
        text_file.write(extracted_text)
    logging.info(f"Text extraction complete. Check '{output_file}' for the output.")
except Exception as e:
    logging.error(f"Error saving extracted text to file: {e}")
    raise