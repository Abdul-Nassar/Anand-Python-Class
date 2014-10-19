import sys
import os

files = os.listdir(sys.argv[1])

def countfilepy(files):
	return [f for f in files if '.py' in f]

print len(countfilepy(files))
