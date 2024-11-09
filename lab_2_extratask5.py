import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(0, 1, 0.01)

def diff_func(z, x):
    y, omega = z

    dy_dx = omega
    domega_dx = (x*omega - 2*y)/(1-x**2)

    return dy_dx, domega_dx

y_0 = 3
omega_0 = 0

z_0 = y_0, omega_0

sol = odeint(diff_func, z_0, x)

plt.plot(x, sol[:, 1], "b", label="dy/dx(t)")
plt.legend()
plt.savefig("extratask5.png")

