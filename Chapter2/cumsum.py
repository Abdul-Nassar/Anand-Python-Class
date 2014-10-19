import sys

def main():
	x = [4, 3, 2, 1]
	cumulative_sum(x)

def cumulative_sum(x):
	s = []
	total = 0
	for i in x:
		total = total + i
		s.append(total)
	print 'Given values : ', x
	print 'Sums : ', s

if __name__=='__main__':
	main()
		
