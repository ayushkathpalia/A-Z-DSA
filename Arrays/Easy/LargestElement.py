Find the largest element in the array.


Approach 1:  O(nlogn)
Sort the array and return the last element.


def largest():
	arr.sort()
	return arr[len(arr)-1]


Approach 2: O(n)
Assigning first element to max varible.
Iterate through the array and check if ele is grater than the max variable     
if yes then assign it to max variable.

OR


use max function to check max btw ele and res & assign to res variable

def largest():
	res = arr[0]
	for ele in arr:
		res = max(res,ele)

	return res



Approach 3:

return max(array)
