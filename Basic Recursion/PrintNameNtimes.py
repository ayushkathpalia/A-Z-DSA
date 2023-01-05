#Print Name N times using Recursion

def printNos(n):
	
	#base case
	if n == 0:
		return 

	printNos(n-1)
	print("ABC")

	