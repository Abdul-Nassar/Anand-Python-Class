import sys

def main():
	f = 'foo.txt'
	print 'The Given File is : ', f
	char = charcount(f)
	print 'Number of Characters : ', char
	word = wordcount(f)
	print 'Number of Words : ', word
	lines = linecount(f)
	print 'Number of Lines : ', lines

def charcount(filename):
	return len(open(filename).read())

def wordcount(filename):
	return len(open(filename).read().split())

def linecount(filename):
	return len(open(filename).readlines())

if __name__=='__main__':
	main()
