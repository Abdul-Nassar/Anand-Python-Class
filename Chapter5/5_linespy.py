import os
import sys

def filespy(files):
	for i in files:
		if '.py' in i:
			print i, len(open(i).readlines())

files = os.listdir(sys.argv[1])
filespy(files)
