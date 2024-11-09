import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 1.5, 0.01)

def diff_func(z, t):
    y, omega = z
    print(omega)

    dy_dt = omega
    domega_dt = (1 - dy_dt**2)**(1/2)

    return dy_dt, domega_dt

y_0 = 1
omega_0 = 0

z_0 = y_0, omega_0

sol = odeint(diff_func, z_0, t)

plt.plot(t, sol[:, 1], "b", label="dy/dt(t)")
plt.legend()
plt.savefig("extratask3.png")

