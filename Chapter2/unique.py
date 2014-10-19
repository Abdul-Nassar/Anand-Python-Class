import sys

def main():
	x = [1, 2, 1, 3, 2, 5]
	unique(x)

def unique(x):
	output = []
	for i in x : 
		if i not in output:
			output.append(i)
	print 'Given List : ', x
	print 'Unique in List : ', output

if __name__=='__main__':
	main()
