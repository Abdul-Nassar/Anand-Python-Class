import sys

fname = open(sys.argv[1]).readlines()
width = int(sys.argv[2])

for i in fname:
	new = i
	if len(new) > width:
		if new[width] == " ":
			print new[:width]
			print new[width:]
		else:
			for a in new[width:]:
				if a == ' ':
					j = new[width:].index(a)
					print new[:j+len(new[:width])]
					print new[j+len(new[:width])+1:]
					break
