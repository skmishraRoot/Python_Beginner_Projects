# Simple qr generator using python.

# qrcode is a library which we use to create qr codes
import qrcode 
# Taking user input 
user_link = input('Enter something here to convert : ')
# Image name
user_img = input('Image name :') 
# Generating qr
qr_img = qrcode.make(user_link)
# saving img in current dir
qr_img.save(user_img + '.jpg')