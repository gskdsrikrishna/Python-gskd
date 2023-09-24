import PyPDF2

def merge_pdfs(input_paths, output_path):
    merger = PyPDF2.PdfMerger()
    for path in input_paths:
        merger.append(path)
    merger.write(output_path)
    merger.close()

# Usage
input_paths = ['D:/Py/RAR/CAI1-2.pdf', "D:/Py/RAR/OriginalWord.pdf"]
output_path = 'D:/Py/RAR/merged.pdf'
merge_pdfs(input_paths, output_path)
