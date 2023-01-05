Left Rotate By One


arr = [1,2,3,4,5] => [2,3,4,5,1]
Appraoch: 
we have save the first ele on of the array and then shifted all elements to the left.Put the ele saved in tmp variable to the last index of the arr

O(n),O(1)

def leftbyOne(arr):
	tmp = arr[0]
	for i in range(1,len(arr)):
		arr[i-1] = arr[i]

	arr[len(arr)-1] = tmp
	return arr



Left Rotate By D places

D = 2, n= 5
arr = [1,2,3,4,5] => [3,4,5,1,2]

Approach : Using a Temporary array.Save 1 to D elements in tmp array, left shift the original array and add the temp array to original array.

O(n),O(k)

def LeftByD(arr,k):
	n = len(arr)
	
	if n == 0:
		return
	
	k = k % n

	if k > n:
		return 

	temp = []
	for i in range(k):
		temp.append(arr[i])

	for i in range(n-k):
		arr[i] = arr[i+k]

	for i in range(n-k,n):
		arr[i] = temp[i-n+k]


Approach 2: Reversal Algorithm  -> O(n),O(1)
1.Reverse the 0 to k elements
2.Reverse the k to n-1 elements
3.Reverse the whole array

def LeftByD(arr):
	d = d % n
	
	l,r = 0, d-1
	while l < r:
		arr[l],arr[r] = arr[r],arr[l]
		l+=1
		r-=1

	l,r = d, n-1
	while l < r:
		arr[l],arr[r] = arr[r],arr[l]
		l+=1
		r-=1

	l,r = 0,n-1
	while l < r:
		arr[l],arr[r] = arr[r],arr[l]
		l+=1
		r-=1
