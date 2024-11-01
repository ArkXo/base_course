import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-1, 1, 0.01)

def diff_func(z, t):
    x, y = z

    dx_dt = 3*x - 2*y + np.e**(3*t)/(np.e**t + 1)
    dy_dt = x - np.e**(3*t)/(np.e**t + 1)

    return dx_dt, dy_dt

x_0 = 5
y_0 = -7

z0 = x_0, y_0

sol = odeint(diff_func, z0, t)

plt.plot(t, sol[:, 0], "b", label="x(t)")
plt.plot(t, sol[:, 1], "g", label="y(t)")
plt.legend()
plt.savefig("task2.png")
