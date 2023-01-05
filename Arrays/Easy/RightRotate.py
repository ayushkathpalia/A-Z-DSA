Right Rotate By One

[1,2,3,4,5] => [5,1,2,3,4]

Approach:Save the last element in a tmp variable and shift all elements to right. Assign the 0th val to the temp.

def rightbyOne(arr):
	n = len(arr)
	tmp = arr[n-1]
	for i in range(n-2,-1,-1):
		arr[i+1] = arr[i]
	arr[0] = tmp



Right Rotate By D Places

[1,2,3,4,5] => [4,5,1,2,3]
D = 2
n = 5

Approach 1: Using a Temp Array to save variables


Approach 2: Reversal Algorithm  O(n),O(1)
1.Reverse whole array
2.Reverse the o to k elements
3.Reverse k to n-1 elements



def RightByD(arr):
	d = d % n
	
	l,r = 0,n-1
	while l < r:
		arr[l],arr[r] = arr[r],arr[l]
		l+=1
		r-=1

	l,r = 0,k-1
	while l < r:
		arr[l],arr[r] = arr[r],arr[l]
		l+=1
		r-=1

	l,r = k,n-1
	while l < r:
		arr[l],arr[r] = arr[r],arr[l]
		l+=1
		r-=1