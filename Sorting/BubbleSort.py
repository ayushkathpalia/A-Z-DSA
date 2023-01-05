#Bubble Sort

- Sorting is done from the back.
- After every iteration, the max element reaches to the final position.
- Stable Algorithm-Does not change position of equal elements. 

O(n^2),O(1)

Algorithm:
1.Run i loop till n-1
2.Run j loop till n-i-1
3.Keep swapping the 2 adjacent elemnts if arr[j] > arr[j+1]

# Normal 
def bubbleSort(arr):
	n = len(arr)
	for i in range(n-1):
		for j in range(n-i-1):
			if arr[j] > arr[j+1]:
				arr[j],arr[j+1] = arr[j+1],arr[j]


#Optimised
def bubbleSort(arr):
	n = len(arr)
	for i in range(n-1):
		swapped = False
		for j in range(n-i-1):
			if arr[j] > arr[j+1]:
				arr[j],arr[j+1] = arr[j+1],arr[j]
				swapped = True
		if not swapped:
			return 