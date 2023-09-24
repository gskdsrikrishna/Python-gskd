from reportlab.pdfgen import canvas

def create_pdf():
    c = canvas.Canvas('path/to/output/generated_pdf.pdf')
    # Set font and size
    c.setFont("Helvetica", 12)
    # Write text
    c.drawString(100, 700, "Hello, World!")
    # Draw shapes
    c.setStrokeColorRGB(0, 0, 0)
    c.setFillColorRGB(0.5, 0.5, 0.5)
    c.rect(100, 500, 200, 100, fill=1)
    # Save the canvas
    c.save()

# Usage
create_pdf()
