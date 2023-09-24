import pytesseract
from PIL import Image
import PyPDF2

def perform_ocr_on_pdf(input_path, output_path):
    with open(input_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        writer = PyPDF2.PdfFileWriter()
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            image = page.extract_images()[0]
            image_data = image['image']
            pil_image = Image.frombytes('RGB', (image['width'], image['height']), image_data)
            text = pytesseract.image_to_string(pil_image)
            page.mergePage(PyPDF2.pdf.PageObject.createFromString(text))
            writer.addPage(page)
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)

# Usage
input_path = 'path/to/scanned_pdf.pdf'
output_path = 'path/to/output/ocr_result.pdf'
perform_ocr_on_pdf(input_path, output_path)
