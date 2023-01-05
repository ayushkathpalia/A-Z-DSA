Search Element in Rotated Array 2 (With Duplicates)

Approach 1: Linear Search

Approach 2:Binary Search


def search(arr,target):
	low,high = 0, len(arr)-1
	mid = 0

	while low <= high:
		mid = low + (high - low) // 2

		if arr[mid] == target:
			return mid
		
		elif arr[low] <= arr[mid]: 												#checking if the left array is sorted 
			if arr[low] <= target and arr[mid] >= target: 						#checking if ele exits in btw low and mid
				high = mid -1
			else:
				low = mid + 1
		
		elif arr[mid] > arr[start]: 											#checking if the left array  not sorted:
			if arr[mid] <= target and arr[high] >= target:
				low = mid+1
			else:
				high = mid - 1
		
		else: 																	#if low=mid=high
			low+=1
			high-=1

	return -1 
