from PIL import Image
from pytesseract import image_to_string

filename = './images/1.jpg'
print filename
text = image_to_string(Image.open(filename))
