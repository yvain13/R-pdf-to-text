# PDF to Text Converter API

A FastAPI-based web service that converts PDF files to text. The service accepts base64-encoded PDF files and returns the extracted text.

## Features

- Convert PDF files to text
- RESTful API with FastAPI
- Automatic API documentation
- Docker support
- Ready for deployment on Render

## API Endpoints

- `POST /api/v1/convert-pdf`: Convert PDF to text
- `GET /health`: Health check endpoint
- `GET /docs`: API documentation (Swagger UI)
- `GET /redoc`: Alternative API documentation

## Local Development

1. Clone the repository:
```bash
git clone https://github.com/yourusername/pdf-to-text-api.git
cd pdf-to-text-api
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the server:
```bash
uvicorn app.main:app --reload
```

The API will be available at http://localhost:8000

## Using Docker

1. Build the Docker image:
```bash
docker build -t pdf-to-text-api .
```

2. Run the container:
```bash
docker run -p 8000:8000 pdf-to-text-api
```

## Deployment on Render

1. Push your code to GitHub
2. Create a new Web Service on Render
3. Connect your GitHub repository
4. Render will automatically detect the configuration from `render.yaml`

## Using the Client

```python
from client.pdf_client import PDFConverter

# Create converter instance
converter = PDFConverter(base_url="https://your-api-url.onrender.com")

# Convert PDF to text
text = converter.convert_pdf_to_text("path/to/your/file.pdf")

if text:
    print("Successfully extracted text:")
    print(text)
```

## API Documentation

After starting the server, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
