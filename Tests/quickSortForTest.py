import time
from random import randrange


def partition(data, start, end):
    pivot = start  # pivot

    # a variable to memorize where the
    i = start + 1

    # partition in the array starts from.
    for j in range(start + 1, end + 1):

        # if the current element is smaller
        # or equal to pivot, shift it to the
        # left side of the partition.
        if data[j] <= data[pivot]:
            data[i], data[j] = data[j], data[i]
            i = i + 1

    data[pivot], data[i - 1] = data[i - 1], data[pivot]
    pivot = i - 1
    return (pivot)


def partitionrand(data, start, end):
    pivot = randrange(start, end)

    # Swapping the starting element of
    # the array and the pivot
    data[start], data[pivot] = data[pivot], data[start]
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
