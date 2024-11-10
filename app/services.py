import base64
import io
import PyPDF2
from typing import Optional
import logging

logger = logging.getLogger(__name__)

async def convert_pdf_to_text(pdf_base64: str) -> str:
    """
    Convert base64 encoded PDF to text.
    
    Args:
        pdf_base64 (str): Base64 encoded PDF file
        
    Returns:
        str: Extracted text from the PDF
        
    Raises:
        Exception: If conversion fails
    """
    try:
        # Decode base64 string to bytes
        pdf_bytes = base64.b64decode(pdf_base64)
        
        # Create a BytesIO object
        pdf_file = io.BytesIO(pdf_bytes)
        
        # Read PDF
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        
        # Extract text from all pages
        text = ""
        for page_num, page in enumerate(pdf_reader.pages):
            logger.debug(f"Processing page {page_num + 1}")
            text += page.extract_text() + "\n"
        
        return text.strip()
        
    except base64.binascii.Error as e:
        logger.error("Invalid base64 encoding")
        raise Exception("Invalid PDF file encoding")
    except Exception as e:
        logger.error(f"PDF conversion error: {str(e)}")
        raise Exception(f"Failed to convert PDF: {str(e)}")
