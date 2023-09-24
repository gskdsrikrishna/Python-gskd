import PyPDF2

def rotate_pdf_pages(input_path, output_path, rotation_angle, page_numbers=None):
    with open(input_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        writer = PyPDF2.PdfWriter()
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            if page_numbers is None or (page_num + 1) in page_numbers:
                page.rotate(rotation_angle)
            writer.add_page(page)
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)

# Usage
input_path = 'D:/Py/RAR/CAI1-2.pdf'
output_path = 'D:/Py/RAR/rotated.pdf'
rotation_angle = 90  # Specify the rotation angle in degrees (e.g., 90, 180, 270)
# Specify the page numbers to rotate (optional, pass None to rotate all pages)
page_numbers = [1, 3, 5]  # Rotate specific pages, e.g., page 1, 3, and 5
rotate_pdf_pages(input_path, output_path, rotation_angle, page_numbers)
