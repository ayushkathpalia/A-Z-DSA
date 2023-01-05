#Reverse Integer


n = 123

def reverse(n):
	ans = 0
	while n:
		rem = n % 10
		ans = ans * 10 + rem
		n = n//10
	return ans


#LEETCODE 
#Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range 
#  [-2^31, 2^31 - 1], then return 0.


def reverse(n):
	MIN = -2**31
	MAX = 2**31-1
	ans = 0
	while n:
		rem = int(math.fmod(n,10))
		n = n//10

		if ans > MAX//10 or (res== MAX//10 and rem >= MAX %10):
			return 0
		if ans < MIN//10 or (res== MIN//10 and rem <= MIN %10):
			return 0

		ans = ans *10 + rem
	return ans


#GFG - Reverse Bits
#Given a 32 bit number X, reverse its binary form and print the answer in decimal.

#SOLVEEE 