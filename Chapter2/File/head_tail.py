import sys

f = open(sys.argv[1]).readlines()

if sys.argv[2] == 'head':
	print f[:2]
elif sys.argv[2] == 'tail':
	print f[-3:]
else:
	print 'Less.....'

