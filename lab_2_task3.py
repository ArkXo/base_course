import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(-1, 1, 0.01)

def diff_func(z, x):
    y, omega = z

    dy_dt = omega
    domega_dt = np.sin(x) + np.cos(x)

    return dy_dt, domega_dt

y_0 = 3
omega_0 = 0

z0 = y_0, omega_0

sol = odeint(diff_func, z0, x)

plt.plot(x, sol[:, 1], "g", label="dy/dt(t)")
plt.legend()
plt.savefig("task3.png")
