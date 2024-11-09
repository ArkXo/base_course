import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(0.1, 5, 0.01)

def diff_func(z, x):
    y, omega = z

    dy_dx = omega
    domega_dx = (dy_dx**2 - 3 * y**2 / x**(1/2)) / y

    return dy_dx, domega_dx

y_0 = 0.1
omega_0 = 1

z_0 = y_0, omega_0

sol = odeint(diff_func, z_0, x)

plt.plot(x, sol[:, 1], "b", label="dy/dt(t)")
plt.legend()
plt.savefig("extratask2.png")
