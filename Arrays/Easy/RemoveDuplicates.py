Remove All Duplicates in place from the sorted array


Approach 1 : Use HashSet as it doesnt store duplicates.Put the elements of hashset to the array and return the last index of the non-duplicates. 

O(n),O(n)

def removeDupp(arr):
    hashset = set()
    for ele in arr:
        if ele not in hashset:
            hashset.add(ele)
    i = 0
    for ele in hashset:
        arr[i] = ele
        i+=1
    return i

Approach 2: Using Two pointers. i for putting the non duplicate elements and j for iterating through the array and getting new elements.
we check if jth element != j-1 th element, then we add value to i ith place and increment i.

O(n),O(1)

def removeDupp(arr):
	i = 1
	for j in range(1,len(arr)):
		if arr[j] != arr[j-1]:
			arr[i] = arr[j]
			i+=1
	return i

