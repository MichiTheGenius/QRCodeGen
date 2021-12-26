import qrcode

def makeQR(name,msg): 
    img = qrcode.make(msg)
    img.save(name)


makeQR('myQR.png','Hello, World!')
