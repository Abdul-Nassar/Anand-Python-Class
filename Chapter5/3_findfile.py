import os
import sys

def findfile(dirname):
	files = os.listdir(dirname)
	for i in files:
			print os.path.abspath(dirname+'/'+i)
			if os.path.isdir(os.path.abspath(dirname+'/'+i)) is True:
				findfile(dirname+'/'+i)
	##print files

findfile(sys.argv[1])

