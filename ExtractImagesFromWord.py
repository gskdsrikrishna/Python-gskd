from docx import Document
from docx.enum.dml import MSO_THEME_COLOR

def extract_images_from_word(input_file):
    doc = Document(input_file)
    images = []
    
    for rel in doc.part.rels.values():
        if "image" in rel.reltype:
            image = rel.target_part.blob
            images.append(image)
    
    return images

# Usage example
input_path = 'path/to/document.docx'
extracted_images = extract_images_from_word(input_path)
for i, image in enumerate(extracted_images):
    with open(f'path/to/image_{i+1}.jpg', 'wb') as f:
        f.write(image)
