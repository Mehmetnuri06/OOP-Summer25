import qrcode
url = 'https://nuri-warsaw-webspace.lovable.app/'
qr = qrcode.make(url)
qr.save("nuri_qr.png")
