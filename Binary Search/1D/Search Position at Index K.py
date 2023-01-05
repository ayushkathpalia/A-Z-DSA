Search Position at Index K.

Approach: The while loop will end when low > end.
so the ans can be low or end+1

O(nlogn)

def searchInsertK(arr, n, k):
    # code here
    low,high = 0,n-1
    mid = 0
    ans = 0
    while low <= high:
        mid = (low+high)//2
        if arr[mid] < k:
            low = mid+1
        elif arr[mid] > k:
            high = mid-1
        else:
            return mid
    return low