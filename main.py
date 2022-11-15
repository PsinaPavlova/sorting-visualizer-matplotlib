from random import sample

from Animations.SortAlgoritmAnimation import AnimateSortAlgoritm
from Tests.TestingSortingAlgoritms import AlgoritmSortingComaparasion

from Tests.BuiltInSortForTest import measurebuiltInSortTime
from Tests.InsertionSortForTest import measureInsertionSortTime
from Tests.quickSortForTest import measureQuickSortTime


tasks = {'1': AnimateSortAlgoritm,
         '2': AlgoritmSortingComaparasion}

try:
    data_size = int(input('Data size(defaut 20):'))
except ValueError:
    data_size = 20


data = sample(range(data_size), data_size)

print('Sorted list: ', sorted(data))
print(data)
print('Time spent on QuickSort using Random Pivoting', measureQuickSortTime(data))
print('Time spent on InsertionSort', measureInsertionSortTime(data))
print('Time spent on BuiltInSort', measurebuiltInSortTime(data))

task = input(
    'Select the task (1 for Sorting Animation, 2 for Sorting algoritms comparasion)')
if task not in tasks:
    task = '1'


func = tasks[task]
func()
