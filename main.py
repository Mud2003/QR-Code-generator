import pyqrcode
from pyqrcode import QRCode

# String which represent the QR code
s = "URL you want profile in QR"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the png file naming "myqr.png"
url.svg("MyFB.svg", scale=6)