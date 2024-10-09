import cv2
from pyzbar.pyzbar import decode

# Load the image using OpenCV
image_cv = cv2.imread(image_path)

# Decode the QR code from the image
qr_codes = decode(image_cv)

# Extract the data from the QR code if found
qr_data = [qr_code.data.decode('utf-8') for qr_code in qr_codes]
qr_data
