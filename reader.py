import fitz  # PyMuPDF

def extract_text_from_pdf(file):
    pdf = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in pdf:
        content = page.get_text()
        lines = content.split("\n")
        cleaned_lines = [line for line in lines if not line.strip().isdigit()]
        text += " ".join(cleaned_lines) + "\n"
    return text.strip()

