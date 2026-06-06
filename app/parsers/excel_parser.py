import pandas as pd
import io

def parse_excel(file_bytes):
    """
    Parses an Excel file stream from memory and converts all sheets into Markdown tables.
    """
    markdown_lines = []
    
    # Read all sheets from the Excel file
    excel_data = pd.read_excel(io.BytesIO(file_bytes), sheet_name=None)
    
    for sheet_name, df in excel_data.items():
        markdown_lines.append(f"## Sheet: {sheet_name}\n")
        
        if df.empty:
            markdown_lines.append("*Empty Sheet*\n")
        else:
            # Replace blank cells with empty strings to keep tables clean
            df = df.fillna("")
            
            # Convert the dataframe directly to a Markdown table
            markdown_lines.append(df.to_markdown(index=False))
            markdown_lines.append("\n")
            
    return "\n".join(markdown_lines)