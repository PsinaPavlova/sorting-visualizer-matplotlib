import math
import random

import matplotlib.pyplot as plt
from Animations.animate import alg_title, camera
from Animations.InsertionSort import InsertionSort
from Animations.quicksort import quickSort


def AnimateSortAlgoritm():

    data_size = 30

    data = random.sample(range(data_size), data_size)

    algorithms = {'1': InsertionSort,
                  '2': quickSort}

    alg = input(
        'Select the algorithm(1 for InsertionSort, 2 for QuickSort using Random Pivoting):')
    if alg not in algorithms:
        alg = '1'

    alg_title(alg)

    func = algorithms[alg]

    if func == quickSort:
        func(data, 0, len(data) - 1)
    elif func == InsertionSort:
        func(data)

    interval_time = 20
    animation = camera.animate(interval=interval_time)

    plt.show()
