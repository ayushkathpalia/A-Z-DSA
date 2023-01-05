Largest Odd no in a String

Approach : O(n),O(1)

String Manipulation 



def largest_odd(num):
	for i in range(len(num)-1,-1,-1):
		if int(num[i])%2 != 0:
			return num[:i+1]
	return ""


