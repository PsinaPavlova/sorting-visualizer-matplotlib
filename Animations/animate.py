import matplotlib.pyplot as plt
from celluloid import Camera

fig = plt.figure()
camera = Camera(fig)
comparisons = 0
graph = plt.bar
titles = {'1': "Insertionsort algorithm",
          '2': 'Quicksort algorithm'}


def alg_title(alg):
    global title
    title = titles[alg]
    return title

# Plot data set and variable to highlight


def Plot(highlight, data):
    x = list(range(len(data)))
    global comparisons
    comparisons += 1

    colors = list(len(data) * 'b')
    colors[highlight] = 'r'
    graph(x, data, color=colors)

    plt.title(title)
    plt.xlabel('Data size:{}, Number of comparisons:{}'.format(
        len(data), comparisons))

    camera.snap()
