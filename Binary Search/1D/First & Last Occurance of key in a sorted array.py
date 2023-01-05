First & Last Occurance of key in a sorted array

Approach 1:Using Linear Search

Approach 2:Using Binary Search

Hint : When the key is equal to mid element. 
First Occurance: Store the mid index to res and assign high to mid-1

Last Occurance: Store the mid index to res and assign low to mid+1

def find(arr,n,x):
    # code here
    def FirstOccurance():
        low = 0
        high = n-1
        ans = -1
        while low <= high:
            mid = (low + high) //2
            if x > arr[mid]:
                low = mid+1
            elif x < arr[mid]:
                high = mid -1
            else:
                ans =  mid
                high = mid - 1
        return ans
    
    def LastOccurance():
        low = 0
        high = n-1
        ans = -1
        while low <= high:
            mid = (low + high) //2
            if x > arr[mid]:
                low = mid+1
            elif x < arr[mid]:
                high = mid -1
            else:
                ans = mid
                low = mid + 1
        return ans
    
    first = FirstOccurance()
    last = LastOccurance()
    return [first,last]
