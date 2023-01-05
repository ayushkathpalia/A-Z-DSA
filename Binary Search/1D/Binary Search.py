Binary Search
- Divide and Conquer



Approach 1 : Iterative  - O(logn),O(1)

def Binary(arr,key):
	low,high = 0,len(arr)-1
	mid = 0

	while low <= high:
		mid = (low+high)//2
		if arr[mid] < key:
			low = mid+1
		elif arr[mid] > key:
			high = mid-1
		else:
			return mid

	return -1



Approach 2 : Recursive   - O(logn),O(logn)


def search(self, nums: List[int], target: int) -> int:
    return self.helper(nums,0,len(nums)-1,target)
    
    
    
def helper(self,nums,low,high,target):
    if low <= high:
        mid = (low+high)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.helper(nums,mid+1,high,target)
        elif nums[mid] > target:
            return self.helper(nums,low,mid-1,target)
    else:
        return -1
