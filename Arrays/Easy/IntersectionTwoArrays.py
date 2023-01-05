Intersection of Two Sorted Arrays

Approach 1:
1. Iterate an array and check if the element is present in the other array.


O(n),O(n)
def intersection(arr1,arr2):
	res=[]
	for ele in arr1:
		if ele in arr2:
			res.append(ele)
	return res


Approach 2:
Using Two Pointers
1.Take two pointers i,j ,start from 0.
2.Increment i if arr1 value is smaller
3.Increment j if arr2 value is smaller
4. Increment both if equal and store value in res.



def intersection(arr1,arr2):
	res = []
	i,j = 0,0
	while i < m and j < n:
		if arr1[i] < arr2[j]:
			i+=1
		elif arr1[i] > arr2[j]:
			j+=1
		else:
			res.append(arr1[i])
			i+=1
			j+=1


Another Way:
    res=list(set(arr1) & set(arr2))
    print(res)
			
