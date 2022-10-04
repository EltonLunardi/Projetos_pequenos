import qrcode
import image

data = 'Phrase'
img = qrcode.make(data)

qr = qrcode.QRCode(version=1, box_size=10, border=5)
img = qr.make_image(fill_color='red', back_color='transparent')

# qr.add_data(data)
# qr.make(fill=True)

img.save('./QRCode_Decodifier/img/tests.png')
