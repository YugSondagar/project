import qrcode as qr

url = input("Enter URL to generate QR: ")
img = qr.make(url)
file_name = input("Enter file name: ")
img.save(file_name)