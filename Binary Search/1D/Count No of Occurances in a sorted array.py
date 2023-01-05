Count No of Occurances in a sorted array

Approach 1:Linear Search . Iterate and count the no of occurances.

Apporach 2:Binary Search. We find the first occurance , then last occurance the return (last-first+1)

O(logn+k)

def firstOccurance(self,arr,n,x):
        low,high = 0,n-1
        mid = 0
        ans = 0
        while low <= high:
            mid = (low+high)//2
            if x > arr[mid]:
                low = mid+1
            elif x < arr[mid]:
                high = mid-1
            else:
                ans = mid
                high = mid-1
        return ans
def lastOccurance(self,arr,n,x):
    low,high = 0,n-1
    mid = 0
    ans = 0
    while low <= high:
        mid = (low+high)//2
        if x > arr[mid]:
            low = mid+1
        elif x < arr[mid]:
            high = mid-1
        else:
            ans = mid
            low = mid+1
    return ans

def count(self,arr, n, x):
	# code here
	if x not in arr:
	    return 0
	first = self.firstOccurance(arr,n,x)
	last = self.lastOccurance(arr,n,x)
	return (last-first+1)
    