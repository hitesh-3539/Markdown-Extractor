from docx import Document

def parse_docx(file_stream):
    """
    Parses a Word document file stream from memory and converts it to Markdown.
    """
    doc = Document(file_stream)
    markdown_lines = []
    
    for paragraph in doc.paragraphs:
        text = paragraph.text.strip()
        if not text:
            continue
            
        # Check paragraph style for headings
        style_name = paragraph.style.name.lower()
        
        if "heading 1" in style_name:
            markdown_lines.append(f"# {text}\n")
        elif "heading 2" in style_name:
            markdown_lines.append(f"## {text}\n")
        elif "heading 3" in style_name:
            markdown_lines.append(f"### {text}\n")
        elif "list bullet" in style_name:
            markdown_lines.append(f"* {text}")
        elif "list number" in style_name:
            markdown_lines.append(f"1. {text}")
        else:
            # Fallback to normal paragraph text
            # Handle inline styling like bold/italic if necessary later
            markdown_lines.append(f"{text}\n")
            
    return "\n".join(markdown_lines)