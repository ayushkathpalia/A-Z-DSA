Peak Element


Apporach 1: Brute Force .Check neighbours.

def peak(arr):

	if arr[0] >= arr[1]:
		return arr[0]

	for i in range(1,len(arr)):
		if arr[i] >= arr[i-1] and arr[i] >= arr[i+1]:
			return arr[i]

	return arr[n-1]



Approach 2: Binary Search 

def peak(arr):
	low = 0
	high = len(arr)-1
	mid = 0

	while low < high:
		mid = (low+high) // 2
		if arr[mid] < arr[mid+1]:
			low = mid+1
		else:
			high = mid
	return high