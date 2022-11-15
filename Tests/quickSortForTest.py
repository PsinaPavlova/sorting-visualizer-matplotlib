import time
from random import randrange


def partition(data, start, end):
    b = (start - 1)  # border
    pivot = data[end]  # pivot

    for i in range(start, end):

        if data[i] <= pivot:
            b += 1
            data[b], data[i] = data[i], data[b]

    data[b + 1], data[end] = data[end], data[b + 1]
    return b + 1


def partitionrand(data, start, end):
    pivot = randrange(start, end)

    data[end], data[pivot] = data[pivot], data[end]
    return partition(data, start, end)


def quickSort(data, start, end):
    if start < end:
        # Return the pivot index
        p = partitionrand(data, start, end)

        # Sort all the elements to the left and to the right of the pivot
        quickSort(data, start, p - 1)
        quickSort(data, p + 1, end)


def measureQuickSortTime(data):
    start = time.time()
    quickSort(data, 0, len(data) - 1)
    return time.time() - start
