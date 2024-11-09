import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-1, 1, 0.01)

def diff_func(omega, t):
    x, y, z = omega

    dx_dt = 3*x - y + z
    dy_dt = x + y + z
    dz_dt = 4*x - y + 4*z

    return dx_dt, dy_dt, dz_dt

x_0 = -71
y_0 = 1
z_0 = -3

omega_0 = x_0, y_0, z_0

sol = odeint(diff_func, omega_0, t)

plt.plot(t, sol[:, 0], "b", label="x(t)")
plt.plot(t, sol[:, 1], "g", label="y(t)")
plt.plot(t, sol[:, 2], "r", label="z(t)")
plt.legend()
plt.savefig("extratask1.png")

