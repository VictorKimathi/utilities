import pytesseract
from PIL import Image

# Load the image
img = Image.open('image2.png')

# Use pytesseract to extract text from the image
text = pytesseract.image_to_string(img)
print(text)
