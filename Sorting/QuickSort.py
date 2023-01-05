Quick Sort

- Divide & Conquer Algo
-O(n^2)
Faster than merge sort
- in place
-tail Recursive
-Partition is key function
-Pivot is chosen for Partition

Partition can be done using two algo:
1.Hoarse
2.Lomuto



def hoarsePartition(arr, l, h):
    pivot = arr[l]

    i = l - 1
    j = h + 1

    while True:

        i = i + 1
        while arr[i] < pivot:
            i = i + 1

        j = j - 1
        while arr[j] > pivot:
            j = j - 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]


def qSort(arr, l, h):
    if l < h:
        p = hoarsePartition(arr, l, h)
        qSort(arr, l, p)
        qSort(arr, p + 1, h)