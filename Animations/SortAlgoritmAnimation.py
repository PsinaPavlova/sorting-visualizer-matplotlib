import random
import math
from quicksort import quickSort
from animate import camera, alg_title
import matplotlib.pyplot as plt
from InsertionSort import InsertionSort


def AnimateSortAlgoritm():
    try:
        data_size = int(input('Data size(defaut 20):'))
    except ValueError:
        data_size = 20

    data = random.sample(range(data_size), data_size)

    algorithms = {'1': InsertionSort,
                  '2': quickSort}

    alg = input(
        'Select the algorithm(1 for InsertionSort, 2 for quickSort):')
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


AnimateSortAlgoritm()
