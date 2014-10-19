import sys
	
def main():
	x = [1, 2, 1, 3, 2, 5]
	dups(x)

def dups(x):
	un = []
	n = []
	for i in x :
		if i not in un:
			un.append(i)
		else:
			n.append(i)
	print 'Given List : ',x	
	print 'Duplicates : ', n				

if __name__=='__main__':
	main()
