#Sum of N Numbers


def sumN(n):
	#base case
	if n == 0:
		return 0
	return n + sumN(n-1)