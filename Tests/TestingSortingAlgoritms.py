from Tests.InsertionSortForTest import measureInsertionSortTime
from Tests.quickSortForTest import measureQuickSortTime
from Tests.BuiltInSortForTest import measurebuiltInSortTime
import matplotlib.pyplot as plt
import random


def AlgoritmSortingComaparasion():
    data = random.sample(range(5000), 5000)
    Length = [10, 50, 100, 500, 1000, 5000]

    QuickSortTimes = [measureQuickSortTime(
        random.sample(range(x), x)) for x in Length]
    InsertionSortTimes = [measureInsertionSortTime(
        random.sample(range(x), x)) for x in Length]
    BuiltInSortTimes = [measurebuiltInSortTime(
        random.sample(range(x), x)) for x in Length]

    plt.plot(Length, QuickSortTimes, color='r')
    plt.plot(Length, InsertionSortTimes, color='b')
    plt.plot(Length, BuiltInSortTimes, color='g')

    plt.title(label="Sort algoritms comparasion\nBuilt In Sort - green | QuickSort - red | Insertion Sort - blue", fontsize=12)

    plt.xlabel("List length")
    plt.ylabel("Time (seconds)")
    plt.annotate("max BuiltInSort Time = " + str(float("{0:.6f}".format(BuiltInSortTimes[5]))), xy=(
        2500, QuickSortTimes[5]+0.2))
    plt.annotate("max QuickSort Time = " + str(float("{0:.6f}".format(QuickSortTimes[5]))), xy=(
        2500, QuickSortTimes[5]+0.4))
    plt.annotate("max InsertionSort Time = " + str(float("{0:.6f}".format(InsertionSortTimes[5]))), xy=(
        2500, QuickSortTimes[5]+0.6))

    plt.show()
