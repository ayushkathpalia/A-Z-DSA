#Selection Sort 
-Selects the min ele from the array
-O(n^2)
-Not Stable - Order of equal elements may change
-In place Algo - No extra memory required


Input: N = 6, array[] = {13,46,24,52,20,9}
Output: 9,13,20,24,46,52

Algorithm:
1. Keep a pointer starting from the array till the length of the array.
2. Find the minimum element from the unsorted/remaining array and swap with the pointer.
3. Increment the pointer.
4. go to point 2.


def selectionSort(arr):
	n = len(arr)
	for i in range(n-1):
		min_index = i
		for j in range(i+1,n):
			if arr[j] < arr[min_index]:
				min_index = j
		arr[i],arr[min_index] = arr[min_index],arr[i]



#GFG
def select(self, arr, i):
    # code here 
    slen = len(arr)
    self.selectionSort(arr,slen)
def selectionSort(self, arr,n):
    #code here
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j] <= arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]