import sys
f = open(sys.argv[1]).readlines()
l = len(max(f))
for i in f:
	p = l-len(i) / 2
	print " "*p +i


