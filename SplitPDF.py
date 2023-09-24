import PyPDF2

def split_pdf(input_path, output_prefix):
    with open(input_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in range(len(reader.pages)):
            writer = PyPDF2.PdfWriter()
            writer.add_page(reader.pages[page])
            output_path = f'{output_prefix}_{page + 1}.pdf'
            with open(output_path, 'wb') as output_file:
                writer.write(output_file)

# Usage
input_path = 'D:/Py/RAR/CAI1-2.pdf'
output_prefix = 'D:/Py/RAR/CAIpdf_page'
split_pdf(input_path, output_prefix)
