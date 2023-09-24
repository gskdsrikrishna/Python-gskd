import tabula

def extract_tables_from_pdf(pdf_path):
    tables = tabula.read_pdf(pdf_path, pages='all')  # Extract tables from all pages
    return tables

# Usage
pdf_path = 'path/to/pdf/file.pdf'
extracted_tables = extract_tables_from_pdf(pdf_path)
for i, table in enumerate(extracted_tables):
    table.to_csv(f'path/to/output/table{i+1}.csv', index=False)
