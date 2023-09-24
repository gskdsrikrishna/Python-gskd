import zipfile

def display_zip_info(zip_file_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        print(f"ZIP File: {zip_file_path}")
        print(f"Number of files: {len(zip_ref.namelist())}")
        print(f"Compressed Size: {zip_ref.file_size} bytes")
        print(f"Uncompressed Size: {zip_ref.extracted_size} bytes")
        print(f"Compression Ratio: {zip_ref.file_size / zip_ref.extracted_size:.2f}")
        print(f"Comments: {zip_ref.comment}")

        print("File List:")
        for file_info in zip_ref.infolist():
            print(f"- {file_info.filename} ({file_info.file_size} bytes)")

# Usage example:
zip_file_path = 'D:/Py/RAR/gskdzip.zip'
display_zip_info(zip_file_path)