from docx import Document

def split_word_document(input_file, chunk_size):
    doc = Document(input_file)
    total_chunks = len(doc.sections) // chunk_size
    
    for i in range(total_chunks):
        start_index = i * chunk_size
        end_index = start_index + chunk_size
        
        split_doc = Document()
        for section in doc.sections[start_index:end_index]:
            for element in section.element.body:
                split_doc.element.body.append(element)
        
        split_doc.save(f'path/to/split_document_{i+1}.docx')

# Usage example
input_path = 'path/to/large_document.docx'
chunk_size = 3  # Number of sections in each split document
split_word_document(input_path, chunk_size)
