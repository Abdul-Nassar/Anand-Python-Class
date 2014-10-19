import sys
def filter(f, n):
	return [x for x in n if even(x) is True]

def even(p):
	return p%2 == 0

m = int(sys.argv[1])
n = [ x for x in range(m)]
print filter(even, n)
