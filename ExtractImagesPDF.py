import PyPDF2
import io
from PIL import Image

def extract_images_from_pdf(pdf_path):
    images = []
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            if '/XObject' in page['/Resources']:
                x_objects = page['/Resources']['/XObject'].getObject()
                for obj in x_objects:
                    if x_objects[obj]['/Subtype'] == '/Image':
                        data = x_objects[obj]._data
                        image = Image.open(io.BytesIO(data))
                        images.append(image)
    return images

# Usage
pdf_path = 'D:/Py/RAR/CAI1-2.pdf'
extracted_images = extract_images_from_pdf(pdf_path)
for i, image in enumerate(extracted_images):
    image.save(f'D:/Py/image.jpg', 'JPEG')
