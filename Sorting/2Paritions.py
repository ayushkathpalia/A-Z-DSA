#Hoares Partition - O(n)

Approach: We use 2 pointers, from start and end. We find element bigger than pivot using i pointer and smaller than pivot using r pointer.
 We swap both the elements. we keep condition till i>=j.

def hoarePartition(arr,l,h):
    pivot=arr[l]
    i=l-1
    j=h+1
    while True:
        i=i+1
        while arr[i]<pivot:
            i=i+1
        j=j-1
        while arr[j]>pivot:
            j=j-1
        if i>=j:
            return j
        arr[i],arr[j]=arr[j],arr[i]






#Lomuto Partition

