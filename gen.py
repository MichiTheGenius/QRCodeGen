import qrcode
import argparse


class Generator():
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='QRCodeGen program')
        self.parser.add_argument(
            'name', type=str, help='name of output QR code')
        self.parser.add_argument(
            'file', type=str, help='input txt file')
        self.args = self.parser.parse_args()

    def makeQR(self, name, msg):
        img = qrcode.make(msg)
        img.save(name)

    def generate(self):
        file_content = self.get_content_from_file(self.args.file)
        self.makeQR(self.args.name, file_content)

    def get_content_from_file(self, file):
        with open(file) as f:
            return f.read()

generator = Generator()

generator.generate()
