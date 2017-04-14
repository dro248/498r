import httplib
import sys
import argparse
import threading
import subprocess
from PIL import Image
from pytesseract import image_to_string


class OCR():
    # pass filename to OCR object
    def __init__(self, filename):
	self.filename = filename

    def run(self):
	print self.filename
	text = image_to_string(Image.open(self.filename))

def parse_options():
    parser = argparse.ArgumentParser(prog='OCRClient', description='A http OCR client', add_help=True)
    parser.add_argument('-n', '--number', type=int, action='store', help='Specify the number of threads to create(deprecated)', default=1)
    return parser.parse_args()

##########################

HOST_PORT = 'localhost:3000'

#create a connection
conn = httplib.HTTPConnection(HOST_PORT)

if __name__ =="__main__":
    args = parse_options()

while True:
    request = "GET localhost:3000"
    request = request.split()
    print "request", request

    # make request
    conn.request(request[0], request[1])
    
    # get response
    response = conn.getresponse()
    index = int(response.read())
    filename = "./images/" + str(index) + ".jpg"

    if index < 0:
	break 

    for i in range(0, args.number):
	myocr = OCR(filename)
	myocr.run()

conn.close()
