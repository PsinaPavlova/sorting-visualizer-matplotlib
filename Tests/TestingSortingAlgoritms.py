from InsertionSortForTest import measureInsertionSortTime
from quickSortForTest import measureQuickSortTime
from BuiltInSortForTest import measurebuiltInSortTime
import matplotlib.pyplot as plt
import random


data = random.sample(range(5000), 5000)


Length = [10, 50, 100, 500, 1000, 5000]


QuickSortTimes = [measureQuickSortTime(
    random.sample(range(x), x)) for x in Length]


InsertionSortTimes = [measureInsertionSortTime(
    random.sample(range(x), x)) for x in Length]

BuiltInSortTimes = [measurebuiltInSortTime(
    random.sample(range(x), x)) for x in Length]


plt.plot(Length, QuickSortTimes)
plt.plot(Length, InsertionSortTimes)
plt.plot(Length, BuiltInSortTimes)

plt.show()
