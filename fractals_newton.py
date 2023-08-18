import math
from itertools import product

import matplotlib.pyplot as plt
import numpy as np

N_SAMPLES = 850
PLOT_MARKER_SIZE = 0.01
MAX_ITER = 100
CONVERGE_DIST = 0.05

samples = np.linspace(-1, 1, N_SAMPLES)
roots = [complex(1, 0), complex(-0.5, math.sqrt(3) * 0.5),
         complex(-0.5, -math.sqrt(3) * 0.5)]


def f(x) -> complex:
    return x ** 3 - 1


def df(x) -> complex:
    return 3 * x ** 2


def newtons_method(x) -> complex or None:
    iter_num = 0
    abs_y = abs(f(x))
    while abs_y > CONVERGE_DIST:
        fx = f(x)
        x = x - fx / df(x)
        iter_num += 1
        if iter_num == MAX_ITER or abs_y > 10e+12:
            return None
        abs_y = abs(fx)
    return x


def append_point(x, y, points_by_root) -> None:
    root = newtons_method(complex(x, y))
    if root is None:
        return

    for r in roots:
        if abs(r - root) < CONVERGE_DIST:
            points_by_root[r].append((x, y))
            break


def calculate() -> dict:
    points_by_root = {r: [] for r in roots}
    for x, y in product(samples, repeat=2):
        append_point(x, y, points_by_root)
    return points_by_root


def plot(roots, points_by_root):
    colors = ['darkblue', 'slateblue', 'lightblue']
    marker_size = 0.01
    color_idx = 0
    for r in roots:
        plt.scatter(*zip(*points_by_root[r]), color=colors[color_idx], s=marker_size)
        color_idx += 1


if __name__ == '__main__':
    points_by_root = calculate()
    plot(roots, points_by_root)
    plt.show()
