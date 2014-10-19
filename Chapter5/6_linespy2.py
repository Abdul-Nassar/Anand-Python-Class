import os
import sys

def filespy(files):
	for i in files:
		if '.py' in i:
#print i
			yield i

def linespy(files):
	for f in files:
		count = 0
		for line in open(f).readlines():
			if line[0] != '#' and line != '\n':
				count = count + 1
		print f, count

files = os.listdir(sys.argv[1])
##print files
pyfiles = filespy(files)
##print pyfiles
linespy(pyfiles)
