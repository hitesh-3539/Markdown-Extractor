from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from datetime import datetime
import io
import zipfile

app = FastAPI(title="Universal Document to Markdown Converter")

# Tell FastAPI to mount the static folder for CSS/HTML
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def serve_frontend():
    with open("static/index.html", "r") as f:
        return f.read()

@app.post("/convert")
async def convert_documents(files: list[UploadFile] = File(...)):
    # Create an in-memory buffer for the zip file
    zip_buffer = io.BytesIO()
    
    with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zip_file:
        for file in files:
            file_bytes = await file.read()
            file_extension = file.filename.split(".")[-1].lower()
            original_name = file.filename.rsplit(".", 1)[0]
            markdown_output = ""
            
            try:
                # Route to the correct parser
                if file_extension == "docx":
                    from app.parsers.docx_parser import parse_docx
                    markdown_output = parse_docx(io.BytesIO(file_bytes))
                    
                elif file_extension in ["xlsx", "xls"]:
                    from app.parsers.excel_parser import parse_excel
                    markdown_output = parse_excel(file_bytes)
                    
                elif file_extension == "pdf":
                    from app.parsers.pdf_parser import parse_pdf
                    markdown_output = parse_pdf(file_bytes)
                    
                elif file_extension == "pptx":
                    from app.parsers.pptx_parser import parse_pptx
                    markdown_output = parse_pptx(file_bytes)
                    
                else:
                    markdown_output = f"Error: .{file_extension} format is not supported."
                
                # Write the text into a new .md file inside the zip
                zip_file.writestr(f"{original_name}_converted.md", markdown_output)
                
            except Exception as e:
                zip_file.writestr(f"{original_name}_error.txt", f"Conversion failed: {str(e)}")
                
    # Reset the buffer's cursor to the beginning
    zip_buffer.seek(0)
    
    # Generate a filename for the zip
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_filename = f"batch_conversion_{timestamp}.zip"
    
    # Send the zip file back to the browser
    return StreamingResponse(
        zip_buffer, 
        media_type="application/x-zip-compressed", 
        headers={"Content-Disposition": f"attachment; filename={zip_filename}"}
    )