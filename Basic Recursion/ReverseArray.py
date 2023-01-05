Reverse Array Using Recusrion



Approach :
1.Take two pointers, i = 0, j = len(arr) -1 
2.Swap  values
3. Increment i and decrement j till i>=j



def rev(arr,i,j):
	if i >= j:
		return
	arr[i],arr[j] = arr[j],arr[i]
	rev(arr,i+1,j-1)

rev(arr,0,len(arr)-1)



Approach 2:
1. use n-i-1 in place of 2nd pointer


def rev(arr,i,n):
	if i >= n/2:
		return
	arr[i],arr[n-i-1] = arr[n-i-1],arr[i]
	rev(arr,i+1,n)
rev(arr,0,len(arr))


