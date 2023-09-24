from docx import Document
from docx.enum import docx

def protect_word_document(input_file, output_file, password=None, editing_permissions=None):
    doc = Document(input_file)
    
    if password:
        doc.encrypt(password)
    
    if editing_permissions:
        protection_type = None
        
        if editing_permissions == 'readOnly':
            protection_type = docx.WdProtectionType.readOnly
        
        elif editing_permissions == 'forms':
            protection_type = docx.WdProtectionType.fillingForms
        
        elif editing_permissions == 'comments':
            protection_type = docx.WdProtectionType.comments
        
        doc.protect(protection_type)
    
    doc.save(output_file)

# Usage example
input_path = 'path/to/document.docx'
output_path = 'path/to/protected_document.docx'
password = 'password123'
editing_permissions = 'readOnly'
protect_word_document(input_path, output_path, password, editing_permissions)
