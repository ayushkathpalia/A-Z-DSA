Floor and Ceil in an unsorted Array


Approach  : sort the array and use Binary Search

O(nlogn)

def getFloorAndCeil(arr, n, x):
    # code here
    arr.sort()
    f,c = -1,-1
    low,high = 0,n-1
    mid = 0
    
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == x:
            return [arr[mid],arr[mid]]
        elif arr[mid] > x:
            c = arr[mid]
            high = mid - 1
        else:
            f = arr[mid]
            low = mid + 1
    return [f,c]


    