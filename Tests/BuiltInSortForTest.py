import time


def measurebuiltInSortTime(data):
    start = time.time()
    data.sort()
    return time.time() - start
