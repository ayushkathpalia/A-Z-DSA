Search Element in Rotated Array


Approach 1: Linear Search ->O(n),O(1)


Approach 2:Binary Search ->O(logn)

Algorithm:
1.while loop for low <= high
2.we check if mid is target.Return mid
3.Check if left array is sorted or not.
4.if sorted check if element exists in btw low and mid(left array),change high, else change low
5.3->else. if target btw mid and high -> change low
6.Change high = mid-1

def search(arr,target):
	low,high = 0, len(arr)-1
	mid = 0

	while low <= high:
		if arr[mid] == target:
			return mid
		if arr[low] <= arr[mid]: #checking if the left array is sorted or not
			if arr[low] <= target and arr[mid] >= target: #checking if ele exits in btw low and mid
				high = mid -1
			else:
				low = mid + 1
		else:
			if arr[mid] <= target and arr[high] >= target:
				low = mid+1
			else:
				high = mid - 1

	return -1 
