import zipfile

def extract_zip_file(zip_file_path, extract_directory):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_directory)

# Usage example:
zip_file_path = "D:/Py/RAR/gskdzip.zip"
extract_directory = 'D:/Py/RAR/'
extract_zip_file(zip_file_path, extract_directory)