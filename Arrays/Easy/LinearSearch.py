Linear Search - Return Index of the key in array if present else -1

arr = [1,2,3,4,5]

def linear(arr,key):
	for i in range(len(arr)):
		if arr[i] == key:
			return i

	return -1