Move All Zeros to the End of the array

Approach 1:  O(n),O(n)
1. Use Temp array.
2. Store all non zero values in the tmp array.
3. And store the remaining zeros at end of the array.

def move(arr):
	tmp = []
	n = len(arr)
	for i in range(n):
		if arr[i] != 0:
			tmp.append(arr[i])
	while i < n:
		tmp.append(0)
		i+=1
	return tmp

Approach 2:  O(n),O(1)
1.Use Two Pointers. i for finding 0 and j for non zero
2. Swap both the elements and incremenet i till next 0.
3.keep increment j to find non negative.

	
[0, 1, 0, 3, 12]
[1, 3, 12, 0, 0]

def move(arr):
	i = 0
	j = 0
	while j < len(arr):
		if arr[j] != 0 :
			arr[i],arr[j] = arr[j],arr[i]
			i+=1
		j+=1

