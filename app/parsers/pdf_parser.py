import pdfplumber
import pytesseract
from pdf2image import convert_from_bytes
import io

def parse_pdf(file_bytes):
    """
    Parses a PDF using digital text and OCR fallback.
    """
    markdown_lines = []
    
    # Open the PDF directly from the bytes we passed in
    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            
            # Smart Fallback for scans and complex languages
            if not text or len(text.strip()) < 10:
                print(f"Page {i+1} appears to be a scan. Triggering OCR engine...")
                images = convert_from_bytes(
                    file_bytes, 
                    first_page=i+1, 
                    last_page=i+1, 
                    dpi=300
                )
                if images:
                    text = pytesseract.image_to_string(images[0], lang='eng+guj+hin')
            
            if text:
                markdown_lines.append(text.strip())
            
            if i < len(pdf.pages) - 1:
                markdown_lines.append("\n---\n")
                
    return "\n\n".join(markdown_lines)