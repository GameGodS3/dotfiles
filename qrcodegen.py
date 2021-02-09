import png
import sys
import pyqrcode

def QRgen(text):
    text = "http://"+text
    url = pyqrcode.create(text)
    url.png('localhost.png', scale = 6) 
if __name__ == "__main__":
   text = sys.argv
   QRgen(text[1])
