#Armstrong Number


Input:153 
Output: Yes, it is an Armstrong Number
Explanation: 1^3 + 5^3 + 3^3 = 153


Algorithm:
1.Get count of Digits.

1.While loop of number
2.Get the last digit using %10 to get remiander
3.Cube digit and add to result.
4.Divide the number using //10 to get divident


def armstrong(n):
    count = 0
    tmp = n
    while tmp :
        rem = tmp % 10
        count+=1
        tmp = tmp//10

	res = 0
	while n:
		digit = n % 10
		res+=(digit**count)
		n = n//10
	return res