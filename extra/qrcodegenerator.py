import qrcode

url=input("enter your url: ").strip()
filepath="C:\\Users\\Admin\\Desktop\\qr.png"


qr=qrcode.QRCode()
qr.add_data(url)

img= qr.make_image()
img.save(filepath)

print("QR Code was generated")