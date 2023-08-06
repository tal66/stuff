import math
import matplotlib.pyplot as plt
import numpy as np

samples = np.linspace(-1, 1, 900)
roots = [complex(1, 0), complex(-0.5, math.sqrt(3) * 0.5),
         complex(-0.5, -math.sqrt(3) * 0.5)]
points_by_root = dict()
for r in roots:
    points_by_root[r] = []


def f(x):
    return x ** 3 - 1


def df(x):
    return 3 * x ** 2


def newtons_method(x):
    max_iter = 400
    abs_y = abs(f(x))
    while abs_y > 0.02 and abs_y < 10e+12:
        fx = f(x)
        x = x - fx / df(x)

        max_iter -= 1
        if max_iter == 0:
            return None

        abs_y = abs(fx)
    return x


def find_root(x, y):
    root = newtons_method(complex(x, y))
    if root is None:
        return
    for r in roots:
        if abs(r - root) < 0.05:
            points_by_root[r].append((x, y))
            break


def plot():
    for y in samples:
        for x in samples:
            find_root(x, y)

    colors = ['darkblue', 'slateblue', 'lightblue']
    color_idx = 0
    for r in roots:
        plt.scatter(*zip(*points_by_root[r]), color=colors[color_idx], s=0.01)
        color_idx += 1
    plt.show()


if __name__ == '__main__':
    plot()
