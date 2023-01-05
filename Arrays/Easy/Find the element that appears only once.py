Find the element that appears only once


N = 5
A = {1, 1, 2, 5, 5}
Output: 2



Approach 1: Use  Dict to store the number and count.And check which element count is 1.


Approach 2: XOR. When two same nos are XOR then it returns 0. So 1 and 1 will return 0, 5 and 5 will return 0. and 2^0 = 2. 2 will be returned.

def once(arr):
	res= 0
	for num in arr:
		res = res ^ num

	return res


