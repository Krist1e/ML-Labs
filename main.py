import matplotlib
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider, Button

from kmeans import *


def draw():
    pass


def main():
    # matplotlib.use('TkAgg')
    plot = plt.subplot(111)
    plt.subplots_adjust(bottom=0.3)

    ax_points = plt.axes((0.1, 0.2, 0.8, 0.05))
    ax_centroids = plt.axes((0.1, 0.15, 0.8, 0.05))
    ax_first_state = plt.axes((0.1, 0.08, 0.35, 0.05))
    ax_last_state = plt.axes((0.55, 0.08, 0.35, 0.05))
    # ax_kmeans_states = plt.axes((0.1, 0.1, 0.8, 0.05))
    ax_calculation = plt.axes((0.1, 0.03, 0.8, 0.05))

    sl_points = Slider(ax_points, 'Points', 1000, 100000, valinit=1000, valstep=1)
    sl_centroids = Slider(ax_centroids, 'Centroids', 2, 20, valinit=10, valstep=1)
    btn_first_state = Button(ax_first_state, 'First State')
    btn_last_state = Button(ax_last_state, 'Last State')
    # sl_kmeans_states = Slider(ax_kmeans_states, 'States', 1, 2, valinit=1, valstep=1)
    btn_calculate = Button(ax_calculation, 'Calculate')

    states = []

    def calculate():
        nonlocal states
        states = kmeans_clustering(int(sl_centroids.val), int(sl_points.val), int(sl_points.valmin), int(sl_points.valmax))
        draw_state(states[0])


    def draw_state(current_state):
        plot.clear()
        current_state.draw_state(plot)
        plt.draw()

    btn_calculate.on_clicked(lambda x: calculate())
    btn_first_state.on_clicked(lambda x: draw_state(states[0]))
    btn_last_state.on_clicked(lambda x: draw_state(states[-1]))

    calculate()

    plt.show()


if __name__ == '__main__':
    main()
