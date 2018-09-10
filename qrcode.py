import qrcode

import random
from PIL import Image
qr = qrcode.QRCode(
    version=10,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=6.7,
    border=5,
)
qr.add_data('amci.net.in')
qr.make(fit=True)
    img = Image.open('1.png')
    img = img.convert("RGBA")
    logo = Image.open('logoo.png')
    box = (135,135,235,235)
    img.crop(box)
    region = logo
    region = region.resize((box[3] - box[0], box[2] - box[1]))
    img.paste(region,box)
    #img = qr.make_image(fill_color="black", back_color="white")
    img.save('1.png')

    