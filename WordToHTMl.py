from docx2html import convert

def convert_word_to_html(input_file, output_file):
    convert(input_file, output_file)

# Usage example
input_path = 'path/to/document.docx'
output_path = 'path/to/document.html'
convert_word_to_html(input_path, output_path)
