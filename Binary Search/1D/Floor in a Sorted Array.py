Floor in a Sorted Array

Approach: when mid element is smaller than K , we change the ans to mid and change low.


def findFloor(self,A,N,K):
    #Your code here
    ans = -1
    low,high = 0,N-1
    
    while low <= high:
        mid=(low+high)//2
        if A[mid] == K:
            return mid
        elif A[mid] < K:
            ans = mid
            low = mid+1
        else:
            high = mid -1
    return ans