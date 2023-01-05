Merge Sort
- Divide  & Conquer Algo - It divides the array in equal parts and then merges the sorted parts.
- Stable
- Not in place


Python inbuild sort Function uses Tim Sort - > Merge sort + Insertion Sort

O(nlogn),O(n)

#GFG
def merge(a, low, mid, high):
    left = a[low:mid + 1]
    right = a[mid + 1:high + 1]

    i = j = 0
    k = low

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            a[k] = left[i]

            k += 1
            i += 1
        else:
            a[k] = right[j]
            k += 1
            j += 1

    while i < len(left):
        a[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        a[k] = right[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    if r > l:
        m = (r + l) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


arr = [10, 5, 30, 15, 7]

mergeSort(arr, 0, 4)
print(*arr)