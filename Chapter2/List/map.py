import sys
n = int(sys.argv[1])

def map(n):
	return [ x*x for x in range(n)]

print map(n)
