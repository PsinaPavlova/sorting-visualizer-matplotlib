import random
import matplotlib.pyplot as plt

from Tests.BuiltInSortForTest import measurebuiltInSortTime
from Tests.InsertionSortForTest import measureInsertionSortTime
from Tests.quickSortForTest import measureQuickSortTime


def AvgTime(func, x):
    data = random.sample(range(x), x)
    sum = 0
    for i in range(10):
        sum += func(data)
    return sum/10


def AlgoritmSortingComaparasion():
    Length = [100, 1000, 2000, 5000, 10000]

    QuickSortTimes = [AvgTime(measureQuickSortTime, x) for x in Length]
    InsertionSortTimes = [AvgTime(measureInsertionSortTime, x) for x in Length]
    BuiltInSortTimes = [AvgTime(measurebuiltInSortTime, x) for x in Length]

    plt.plot(Length, QuickSortTimes, color='r')
    plt.plot(Length, InsertionSortTimes, color='b')
    plt.plot(Length, BuiltInSortTimes, color='g')

    plt.title(label="Sort algoritms comparasion\nBuilt In Sort - green | QuickSort - red | Insertion Sort - blue", fontsize=12)
    plt.xlabel("List length")
    plt.ylabel("Time (seconds)")

    plt.annotate("max BuiltInSort Time = " + str(float("{0:.6f}".format(BuiltInSortTimes[4]))), xy=(
        0, QuickSortTimes[4]+0.3))
    plt.annotate("max QuickSort Time = " + str(float("{0:.6f}".format(QuickSortTimes[4]))), xy=(
        0, QuickSortTimes[4]+0.4))
    plt.annotate("max InsertionSort Time = " + str(float("{0:.6f}".format(InsertionSortTimes[4]))), xy=(
        0, QuickSortTimes[4]+0.5))

    plt.show()
