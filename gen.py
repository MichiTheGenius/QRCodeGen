import qrcode
import argparse



class Generator():
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='QRCodeGen program')
        self.parser.add_argument('name', type=str, help='name of output QR code')
        self.parser.add_argument('content', type=str, help='content of QR code')
        self.args = self.parser.parse_args()
    
    def makeQR(self, name, msg): 
        img = qrcode.make(msg)
        img.save(name)

    def generate(self):
        self.makeQR(self.args.name, self.args.content)


generator = Generator()

generator.generate()
