from pydantic import BaseModel, Field
from typing import Optional

class PDFRequest(BaseModel):
    pdf_base64: str = Field(
        ...,
        description="Base64 encoded PDF file",
        example="JVBERi0xLjcKCjEgMCBvYmoKCjIgMCBvYmoKPDwKL..."
    )

class PDFResponse(BaseModel):
    success: bool = Field(
        ...,
        description="Indicates if the conversion was successful"
    )
    text: Optional[str] = Field(
        None,
        description="Extracted text from the PDF"
    )
    error: Optional[str] = Field(
        None,
        description="Error message if conversion failed"
    )
