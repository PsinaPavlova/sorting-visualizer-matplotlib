import random
import math
from quicksort import quickSort
from bubblesort import bubbleSort
from heapsort import heapSort
from introsort import introSort
from animate import camera, alg_title, graph_title, graphs
import matplotlib.pyplot as plt
from InsertionSort import InsertionSort

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

gph = input('Select the graph(1 for bar, 2 for scatter):')
if gph not in graphs:
    gph = '1'


graph_title(gph)
alg_title(alg)

func = algorithms[alg]

if func == quickSort:
    func(data, 0, len(data) - 1)
elif func == InsertionSort:
    func(data)

interval_time = 20
animation = camera.animate(interval=interval_time)


plt.show()
