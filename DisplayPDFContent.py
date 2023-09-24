import PyPDF2
def pdf_to_text(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text()
        return text

# Usage
pdf_path = "D:/Py/RAR/CAI1-2.pdf"
text_content = pdf_to_text(pdf_path)
print(text_content)