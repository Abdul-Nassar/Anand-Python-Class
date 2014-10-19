import sys

fname = open(sys.argv[1]).readlines()
width = int(sys.argv[2])

for i in fname:
	new = i
	while len(new) > width:
		print new[:width]
		new = new[width:]
	print new


