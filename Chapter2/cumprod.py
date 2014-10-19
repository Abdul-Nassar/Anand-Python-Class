import sys

def main():
	x = [1, 2, 3, 4]
	cumproduct(x)
	y = [4, 3, 2, 1]
	cumproduct(y)


def cumproduct(x):
	prod = []
	p = 1
	for i in x:
		p = p * i
		prod.append(p)
	print 'Given Values : ', x
	print 'Cumulative Product : ', prod

if __name__=='__main__':
	main()
	
