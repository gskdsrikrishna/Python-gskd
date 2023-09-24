import zipfile
import tqdm

def extract_zip_file_with_progress(zip_file_path, extract_directory):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        file_count = len(zip_ref.infolist())
        extracted_count = 0

        with tqdm.tqdm(total=file_count, desc='Extracting', unit='file') as pbar:
            for file_info in zip_ref.infolist():
                zip_ref.extract(file_info, extract_directory)
                extracted_count += 1
                pbar.set_postfix({'progress': f'{extracted_count}/{file_count}'})
                pbar.update(1)

# Usage example:
zip_file_path = "D:/Py/RAR/gskd.zip"
extract_directory = 'extracted_files/'
extract_zip_file_with_progress(zip_file_path, extract_directory)
