Union of Two Arrays


Approach 1: Using Set to store  both arrays.Set removes duplicates. O(n),O(n)

Apporach 2:Two Pointers O(m+n),O(1)
1. Take two pointers i,j from starting of both arrays.
2.Append the smaller ele from both arrays and keep incrementing


def mergeArrays(a,b,n,m):
    i,j = 0,0
    res = []
    while i < m and j < n:
        if a[i] <= b[j]:
            if a[i] not in res:
                res.append(a[i])
            i+=1
        elif b[j] < a[i]: 
            if b[j] not in res:
                res.append(b[j])
            j+=1
    while i < m:
        if a[i] not in res:
            res.append(a[i])
        i+=1
    while j < n:
        if b[j] not in res:
            res.append(b[j])
        j+=1
    return res


Another WAY:
    res= set(a) | set(b)
    return sorted(list(res))