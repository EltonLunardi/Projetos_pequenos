from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('./QRCode/img/sexo.png')
result = decode(img)

print(result)
