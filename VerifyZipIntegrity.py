import zipfile

def verify_zip_integrity(zip_file_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        is_valid = zip_ref.testzip() is None
        if is_valid:
            print("ZIP file integrity check passed.")
        else:
            print("ZIP file integrity check failed.")

# Usage example:
zip_file_path = 'D:/Py/RAR/gskdzip.zip'
verify_zip_integrity(zip_file_path)