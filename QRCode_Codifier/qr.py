import qrcode
import image

data = 'Phrase'
img = qrcode.make(data)

#qr = qrcode.QRCode(version = 1,box_size=10,border=5)

img.save('./QRCode_Decodifier/img/tests.png')

#img.save('DIR')