#Fibonacci Number with Recursion

0,1,1,2,3



def fibo(n):
	if n <= 1:
		return n

	return fibo(n-1)+fibo(n-2)



