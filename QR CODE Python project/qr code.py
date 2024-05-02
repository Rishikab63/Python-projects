# -*- coding: utf-8 -*-

"""
Created on Thu May  2 10:51:07 2024

@author: Rishika
"""

import qrcode as qr


#will generate qr for this link
img= qr.make("https://dispensarydata-85401.web.app/")  #inside quotes give link of page which should open on scanning qr code
# lnk of bit dispensary website ap

#save- qr code with this name
img.save("qrcode_bit_dispensay.png")

#adding some properties to it

'''

import qrcode
from PIL import image

#image ka coloyr, back colo, version, border changing

qr=qrcode.QRCODE(version=1, error_crrection=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4,)

#qr code s related data denge
qr.add_data("https://dispensarydata-85401.web.app/")
#creaking qr ocde
qr.make(fit=True)  #url s data aaya h ..eska true value de denge
#creating it as image
img=qr.make_image(fill_color="red",back_color="blue")

#saving
img.save("qrcode_bit_dispensary.png")


'''










