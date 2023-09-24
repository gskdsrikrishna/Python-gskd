import PyPDF2

def fill_pdf_form(input_path, output_path, field_data):
    with open(input_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        writer = PyPDF2.PdfFileWriter()
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            writer.addPage(page)
            if '/AcroForm' in reader.trailer['/Root']:
                acro_form = reader.trailer['/Root']['/AcroForm'].getObject()
                if acro_form is not None:
                    for field in acro_form['/Fields']:
                        field_name = field.getObject()['/T']
                        if field_name in field_data:
                            field_value = field_data[field_name]
                            writer.getFormTextFields()[field_name] = field_value
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)

# Usage
input_path = 'path/to/pdf/form.pdf'
output_path = 'path/to/output/filled_form.pdf'
field_data = {
    'name': 'John Doe',
    'email': 'johndoe@example.com',
    'phone': '123-456-7890'
}
fill_pdf_form(input_path, output_path, field_data)
