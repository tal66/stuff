import numpy as np
from matplotlib import pyplot as plt

from convex_hull import plot_convex_hull, plot_points, Point

coeff = [1, -1, 3, -1, 0, -3]
p = np.poly1d(coeff)
derivative = np.polyder(p)

roots = np.roots(coeff)
roots_d = derivative.roots

plot_points([Point(np.real(root), np.imag(root)) for root in roots_d], 'darkblue')
plot_convex_hull([Point(np.real(root), np.imag(root)) for root in roots])
plt.ylabel('Im(x)')
plt.xlabel('Re(x)')
plt.show()
