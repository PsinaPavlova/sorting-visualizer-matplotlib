from Animations.SortAlgoritmAnimation import AnimateSortAlgoritm

from Tests.TestingSortingAlgoritms import AlgoritmSortingComaparasion

tasks = {'1': AnimateSortAlgoritm,
         '2': AlgoritmSortingComaparasion}

task = input(
    'Select the task (1 for Sorting Animation, 2 for Sorting algoritms comparasion)')
if task not in tasks:
    task = '1'

func = tasks[task]
func()
