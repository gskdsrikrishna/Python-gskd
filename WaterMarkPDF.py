import PyPDF2

def watermark_pdf(input_path, output_path, watermark_path, text=None):
    with open(input_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        writer = PyPDF2.PdfWriter()
        watermark = PyPDF2.PdfReader(watermark_path)
        if text:
            watermark_page = watermark.getPage(0)
            watermark_page.mergePage(PyPDF2.pdf.PageObject.createBlankPage(reader.getPage(0).mediaBox.getWidth(), reader.getPage(0).mediaBox.getHeight()))
            watermark_page.mergePage(PyPDF2.pdf.PageObject.createBlankPage(reader.getPage(0).mediaBox.getWidth(), reader.getPage(0).mediaBox.getHeight()))
            watermark_page.mergePage(PyPDF2.pdf.PageObject.createBlankPage(reader.getPage(0).mediaBox.getWidth(), reader.getPage(0).mediaBox.getHeight()))
            watermark_page.mergePage(PyPDF2.pdf.PageObject.createBlankPage(reader.getPage(0).mediaBox.getWidth(), reader.getPage(0).mediaBox.getHeight()))
            watermark_page.mergePage(PyPDF2.pdf.PageObject.createBlankPage(reader.getPage(0).mediaBox.getWidth(), reader.getPage(0).mediaBox.getHeight()))
            watermark_page.mergePage(PyPDF2.pdf.PageObject.createBlankPage(reader.getPage(0).mediaBox.getWidth(), reader.getPage(0).mediaBox.getHeight()))
            watermark_page.mergePage(PyPDF2.pdf.PageObject.createBlankPage(reader.getPage(0).mediaBox.getWidth(), reader.getPage(0).mediaBox.getHeight()))
            watermark_page.mergePage(PyPDF2.pdf.PageObject.createBlankPage(reader.getPage(0).mediaBox.getWidth(), reader.getPage(0).mediaBox.getHeight()))
            watermark_page.mergePage(PyPDF2.pdf.PageObject.createBlankPage(reader.getPage(0).mediaBox.getWidth(), reader.getPage(0).mediaBox.getHeight()))
            watermark_page.mergePage(PyPDF2.pdf.PageObject.createBlankPage(reader.getPage(0).mediaBox.getWidth(), reader.getPage(0).mediaBox.getHeight()))
            watermark_page.mergePage(PyPDF2.pdf.PageObject.createBlankPage(reader.getPage(0).mediaBox.getWidth(), reader.getPage(0).mediaBox.getHeight()))
            watermark_page.mergePage(PyPDF2.pdf.PageObject.createBlankPage(reader.getPage(0).mediaBox.getWidth(), reader.getPage(0).mediaBox.getHeight()))
            watermark_page.mergePage(PyPDF2.pdf.PageObject.createBlankPage(reader.getPage(0).mediaBox.getWidth(), reader.getPage(0).mediaBox.getHeight()))
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            if watermark_path.endswith('.pdf'):
                page.mergePage(watermark_page)
            elif watermark_path.endswith(('.jpg', '.jpeg', '.png')):
                watermark_image = PyPDF2.pdf.Image(watermark_path)
                watermark_image.scaleToFit(page.mediaBox.getWidth(), page.mediaBox.getHeight())
                page.mergeScaledTranslatedPage(watermark_image, 0, 0)
            if text:
                page.mergeScaledTranslatedPage(watermark_page, 0, 0)
                page.mergeScaledTranslatedPage(watermark_page, 0, 0)
            writer.addPage(page)
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)

# Usage
input_path = 'D:/Py/RAR/CAI1-2.pdf'
output_path = 'D:/Py/RAR/watermarked.pdf'
watermark_path = 'D:/Py/RAR/gskd1.jpg'  # Provide the path to the watermark image or PDF file
text = 'Confidential'  # Optional: Specify the text for watermarking (None for image watermark)
watermark_pdf(input_path, output_path, watermark_path, text)
