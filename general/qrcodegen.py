import png
import sys
import pyqrcode

def QRgen(text):
    if (text[0:7]=="http://"):
        text = text[7:]
    elif (text[0:8]=="https://"):
        text = text[8:]
    text = "http://"+text
    url = pyqrcode.create(text)
    url.png('localhost.png', scale = 6) 
if __name__ == "__main__":
   text = sys.argv
   QRgen(text[1])
