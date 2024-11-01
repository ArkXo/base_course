import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.01)

def diff_func(z, x):
    y, z = z

    dy_dx = y**2 *z
    dz_dx = z/x - y * x**2

    return dy_dx, dz_dx

y_0 = 1
z_0 = -3

z0 = y_0, z_0

sol = odeint(diff_func, z0, x)

plt.plot(x, sol[:, 0], "b", label="y(t)")
plt.plot(x, sol[:, 1], "g", label="z(t)")
plt.legend
plt.savefig("task1.png")

