from fpdf import FPDF
import glob

def convert_images_to_pdf(image_folder, output_path):
    image_files = glob.glob(f'{image_folder}/*.jpg')  # Modify the file extension based on your image types
    pdf = FPDF()
    for image_file in image_files:
        pdf.add_page()
        pdf.image(image_file, x=0, y=0, w=210, h=297)  # Modify the page size as needed
    pdf.output(output_path, 'F')

# Usage
image_folder = 'path/to/image/folder'
output_path = 'path/to/output/images.pdf'
convert_images_to_pdf(image_folder, output_path)
