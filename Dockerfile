# Use a lightweight Python image as the base
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies required by Tesseract and pdf2image
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-eng \
    tesseract-ocr-hin \
    tesseract-ocr-guj \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

# Copy your requirements file first to cache dependencies
COPY requirements.txt .

# Install the Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container
COPY . .

# Expose the port FastAPI will run on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]