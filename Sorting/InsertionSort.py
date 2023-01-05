#Insertion Sort
-In-place
-Stable
-Used for small arrays

O(n^2)


we start fromm 1 and every iteration of i, we take next element and put it to its correct postion using while j loop.


Algorithm:
1.Loop from 1 to len(arr)
2.take curr element ,j = i-1
3.Check using while if j >= 0  and curr val < arr[j]
4.keep decrementing j for the curr to get the positon



def insertionSort(arr):
	for i in range(1,len(arr)):
		curr = arr[i]
		j = i-1
		while j >= 0 and curr < arr[j]:
			arr[j+1] = arr[j]
			j-=1
		arr[j+1] = curr