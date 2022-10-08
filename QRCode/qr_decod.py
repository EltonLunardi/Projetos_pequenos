from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('./QRCode/img/test.png')
result = decode(img)

print(result)
