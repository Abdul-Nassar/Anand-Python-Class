import sys

def main():
	f = open('foo.txt', 'r')
	list1 = f.readlines()
	for line in range(len(list1)-1, -1, -1):
		print reverse(list1[line])

if __name__=='__main__':
	main()
	
