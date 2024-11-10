from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .schemas import PDFRequest, PDFResponse
from .services import convert_pdf_to_text
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="PDF to Text Converter API",
    description="A service that converts PDF files (base64 encoded) to text",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.post("/api/v1/convert-pdf", response_model=PDFResponse)
async def convert_pdf(request: PDFRequest):
    """
    Convert a base64 encoded PDF file to text.
    """
    try:
        logger.info("Received PDF conversion request")
        text = await convert_pdf_to_text(request.pdf_base64)
        logger.info("PDF conversion successful")
        return PDFResponse(success=True, text=text)
    except Exception as e:
        logger.error(f"PDF conversion failed: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

@app.get("/health")
async def health_check():
    """
    Health check endpoint for monitoring.
    """
    return {"status": "healthy"}

@app.get("/")
async def root():
    """
    Root endpoint with API information.
    """
    return {
        "message": "Welcome to PDF to Text Converter API",
        "docs": "/docs",
        "health": "/health"
    }
