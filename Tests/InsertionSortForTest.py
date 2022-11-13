import time


def InsertionSort(data):
    for i in range(len(data)):
        j = i - 1
        key = data[i]
        while data[j] > key and j >= 0:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key


def measureInsertionSortTime(data):
    start = time.time()
    InsertionSort(data)
    return time.time() - start
