import pytesseract
from PIL import Image
import pdfplumber
import os

def perform_ocr(file_path):
    """
    Perform OCR on the specified file path.
    Supports images and PDFs.

    Args:
    file_path (str): Full path to the file to be processed.

    Returns:
    str: Extracted text from the file or None if an error occurs.
    """
    _, file_extension = os.path.splitext(file_path)
    text = ""

    try:
        if file_extension.lower() in ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']:
            text = pytesseract.image_to_string(Image.open(file_path))
        elif file_extension.lower() == '.pdf':
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text
                    else:
                        raise ValueError(f"No text could be extracted from page of {file_path}")
        else:
            raise ValueError("Unsupported file type")
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
        text = None

    return text

def classify_document(text):
    """
    Classify the extracted text into predefined categories.

    Args:
    text (str): Text extracted from the document.

    Returns:
    str: Document category based on content ('facture', 'pièce_d_identité', 'autre', 'error').
    """
    if text is None:
        return "error"
    if "facture" in text.lower():
        return "facture"
    elif "identité" in text.lower():
        return "pièce_d_identité"
    else:
        return "autre"

def process_file(file_path):
    """
    Coordinate the OCR and document classification.

    Args:
    file_path (str): Full path to the file to be processed.

    Returns:
    str: Classification result or an error message.
    """
    text = perform_ocr(file_path)
    if text is not None:
        doc_type = classify_document(text)
        return doc_type
    else:
        return "error_processing_file"

def process_all_files_in_directory(directory_path):
    """
    Process all files in the specified directory.

    Args:
    directory_path (str): Path to the directory containing files to process.
    """
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.pdf')):
            result = process_file(file_path)
            print(f"Processing result for {file_path}: {result}")
        else:
            print(f"Skipping unsupported file type for {file_path}")

if __name__ == "__main__":
    directory_path = os.path.abspath("../input_documents")  # Convert relative path to absolute
    process_all_files_in_directory(directory_path)
