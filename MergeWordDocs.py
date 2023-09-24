from docx import Document

def merge_word_documents(output_file, *input_files):
    merged_doc = Document()
    
    for file in input_files:
        doc = Document(file)
        for element in doc.element.body:
            merged_doc.element.body.append(element)
    
    merged_doc.save(output_file)

# Usage example
output_path = 'path/to/merged_document.docx'
input_paths = ['path/to/document1.docx', 'path/to/document2.docx', 'path/to/document3.docx']
merge_word_documents(output_path, *input_paths)
