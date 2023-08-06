import matplotlib.pyplot as plt
import numpy as np

x_range = np.linspace(-2, 0.5, 200)
y_range = np.linspace(-1.0, 1.0, 200)
converge_list = []
max_iter = 500
power = 2
points = []

for y in y_range:
    for x in x_range:
        c = complex(x, y)
        zn = c
        bounded = True

        for i in range(0, max_iter):
            zn = pow(zn, power) + c
            if (zn.real ** 2 + zn.imag ** 2) >= 4:
                bounded = False
                break

        if bounded:
            points.append((x,y))

plt.scatter(*zip(*points), color='black', s=3)
plt.show()