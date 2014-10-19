import sys

filename = sys.argv[1]
f = open(filename).readlines()
for i in f:
	if sys.argv[2] in i:
		print i
