import PyPDF2

def encrypt_pdf(input_path, output_path, password):
    with open(input_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        writer = PyPDF2.PdfWriter()
        for page_num in range(len(reader.pages)):
            writer.add_page(reader.pages[page_num])
        writer.encrypt(password)
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)

# Usage
input_path = 'D:/Py/RAR/CAI1-2.pdf'
output_path = 'D:/Py/RAR/encrypted.pdf'
password = 'gskd'
encrypt_pdf(input_path, output_path, password)
