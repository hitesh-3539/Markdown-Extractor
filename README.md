# Universal Markdown Extractor 

A RAG-optimized extraction tool that converts unstructured PDFs, Word documents, Excel sheets, and PPTX files into clean, structured Markdown to drastically reduce LLM token waste and improve context processing.

## The Problem it Solves
When feeding raw documents to Large Language Models (LLMs), invisible formatting, metadata, and erratic spacing consume thousands of unnecessary API tokens and confuse RAG pipelines. **Markdown Extractor** acts as a data ingestion engine that strips away the bloat, leaving only clean, AI-ready text.

## Key Features
* **LLM Token Optimization:** Outputs strictly structured Markdown, maximizing your AI context window and minimizing API costs.
* **100% Stateless & Private:** Zero database connections (`database.py` is entirely empty by design). No user documents are ever saved, stored, or logged on the server.
* **In-Memory Zip Processing:** Handles large batch uploads by buffering files in the server's RAM using `io.BytesIO` and instantly returning a neat `.zip` archive, preventing local hard drive clutter.
* **Smart OCR Fallback:** Integrated Tesseract OCR automatically detects and parses text from scanned PDFs and complex image-based documents.
* **Production-Ready Docker:** Fully containerized with a comprehensive `Dockerfile` that automatically handles heavy Linux system dependencies like Poppler and Tesseract.

## Visual Showcase

### 1. The Workspace
A sleek, glassmorphism-styled UI for frictionless drag-and-drop ingestion.
<img width="1470" height="800" alt="Screenshot 2026-06-06 at 5 15 08 PM" src="https://github.com/user-attachments/assets/abc6c5c8-4d24-43b6-85ea-7131700faeb8" />


### 2. Batch Processing
Files are processed sequentially to protect server memory, then bundled into a single ZIP file.
<img width="1470" height="800" alt="Screenshot 2026-06-06 at 5 15 35 PM" src="https://github.com/user-attachments/assets/9877b2b3-4b96-459d-b948-94c83c62a1a0" />


### 3. The Output
Complex academic and technical notes are perfectly converted into structured Markdown, ready for an LLM.
<img width="1470" height="956" alt="Screenshot 2026-06-06 at 5 17 43 PM" src="https://github.com/user-attachments/assets/e4e78ecc-0315-476c-8b29-9597bbde116c" />


## 🛠️ Tech Stack
* **Backend:** Python, FastAPI, Uvicorn
* **Document Parsing:** `pdfplumber`, `python-docx`, `pandas`, `python-pptx`
* **OCR Engine:** Tesseract (`pytesseract`), `pdf2image`, Poppler
* **Frontend:** Vanilla HTML5, CSS3, JavaScript
* **Deployment:** Docker

## Local Setup & Installation

### Option 1: Run via Docker (Recommended)
Because this project requires system-level dependencies (Tesseract & Poppler), Docker is the easiest way to run it anywhere.
```bash
# Clone the repository
git clone [https://github.com/YOUR_USERNAME/markdown-extractor.git](https://github.com/YOUR_USERNAME/markdown-extractor.git)
cd markdown-extractor

# Build the Docker image
docker build -t markdown-extractor .

# Run the container
docker run -p 8000:8000 markdown-extractor
