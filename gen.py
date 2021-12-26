import qrcode

def makeQR(name,msg): 
    img = qrcode.make(msg)
    img.save(name)


name = input('Enter filename of the QR code: ')
content = input('Enter the content of the QR code: ')

makeQR(name,content)
