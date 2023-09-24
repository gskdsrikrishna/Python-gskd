#QR Code Generatoe with Python
import pyqrcode 
from pyqrcode import QRCode 
# String which represent the QR code 
s = "https://www.youtube.com"
# Generate QR code 
url = pyqrcode.create(s) 
# Create and save the png file nami