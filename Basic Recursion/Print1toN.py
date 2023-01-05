#Print 1 to N using Recursion

def printNos(n):
	
	#base case
	if n == 0:
		return 

	printNos(n-1)
	print(n,end="")

	