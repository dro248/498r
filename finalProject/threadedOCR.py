import argparse
import sys
import threading
import subprocess
from PIL import Image
from pytesseract import image_to_string


class OCR(threading.Thread):
    # pass filename to thread
    def __init__(self, filename):
        threading.Thread.__init__(self)
	self.filename = filename

    def run(self):
        #print "Hello from thread",self.getName()
	print self.filename	
	text = image_to_string(Image.open(self.filename))

def parse_options():
        parser = argparse.ArgumentParser(prog='threadHello', description='Simple demonstration of threading', add_help=True)
        parser.add_argument('-n', '--number', type=int, action='store', help='Specify the number of threads to create',default=10)
        return parser.parse_args()

if __name__ == "__main__":
    args = parse_options()

    # create threads (somewhat expensive)
    threads = []
    for i in range(0,args.number):
	filename = './images/' + str(i+1) + '.jpg'
	h = OCR(filename)
	threads.append(h)

    # run threads
    for t in threads:
        t.start()

    # kill threads (when finished)
    for t in threads:
        t.join()

