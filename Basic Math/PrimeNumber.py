#Prime Number

Prime number has 2 factors, 1 and no itself.


Edge Case: check if n == 1.

#Brute Force: - O(n),O(1)

Algorithm:
1.Run loop from 2 to n.
2.Check if no is divisible by i. If yes that means more factors,so return False
3.return True at end 

def prime(n):
	for i in range(2,n):
		if n % i == 0:
			return False


	return True



#Optimized Approach - O(sqrt(n)),O(1)

Algorithm:
1.Run loop from 2 to sqrt(n)
2.Check if no is divisible by i. If yes that means more factors,so return False
3.Return True at end


def prime(n):
	for i in range(2,sqrt(n)):
		if n & i == 0:
			return False

	return True