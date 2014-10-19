import sys
import os

n = int(sys.argv[1])
lines = open(sys.argv[2]).readlines()

i = 0
def split(lines, i):
	fname = 'File%d'%i
	f = open(fname, 'a')
	if len(lines) >= n:
		for j in range(n):
			f.write(lines[j])
		split(lines[3:], i + 1)
	else:
		for j in range(len(lines)):
			f.write(lines[j])

split(lines, i)
