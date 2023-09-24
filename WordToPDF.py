import os
import win32com.client as win32

def convert_word_to_pdf(input_file, output_file):
    word = win32.gencache.EnsureDispatch('Word.Application')
    doc = word.Documents.Open(input_file)
    doc.SaveAs(output_file, FileFormat=17)
    doc.Close()
    word.Quit()

# Usage example
input_path = 'path/to/document.docx'
output_path = 'path/to/document.pdf'
convert_word_to_pdf(input_path, output_path)
