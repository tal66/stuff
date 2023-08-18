from itertools import product
import matplotlib.pyplot as plt
import numpy as np

MAX_ITER = 400
PLOT_MARKER_SIZE = 3
N_SAMPLES = 200
POWER = 2
ESCAPE_RADIUS = 2

x_range = np.linspace(-2, 0.5, N_SAMPLES)
y_range = np.linspace(-1.0, 1.0, N_SAMPLES)
points = []

for (x,y) in product(x_range, y_range):
    c = complex(x, y)
    zn = c
    bounded = True

    for i in range(0, MAX_ITER):
        zn = pow(zn, POWER) + c
        if (zn.real ** 2 + zn.imag ** 2) > ESCAPE_RADIUS ** 2:
            bounded = False
            break

    if bounded:
        points.append((x,y))

plt.scatter(*zip(*points), color='black', s=PLOT_MARKER_SIZE)
plt.show()