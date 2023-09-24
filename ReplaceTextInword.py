from docx import Document

def replace_text_in_word(input_file, output_file, search_text, replace_text):
    doc = Document(input_file)
    
    for paragraph in doc.paragraphs:
        if search_text in paragraph.text:
            paragraph.text = paragraph.text.replace(search_text, replace_text)
    
    doc.save(output_file)

# Usage example
input_path = 'path/to/document.docx'
output_path = 'path/to/modified_document.docx'
search_text = 'replace'
replace_text = 'replacement'
replace_text_in_word(input_path, output_path, search_text, replace_text)
