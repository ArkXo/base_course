import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x_0 = np.arange(-1, 0, 0.01)
x_1 = np.arange(0.01, 1, 0.01)

def diff_func(z, x):
    y, omega = z

    dy_dt = omega
    domega_dt = ( (4*x**2 +  1/2)*y - x*omega ) / x**2

    return dy_dt, domega_dt

y_0 = 3
omega_0 = 0
z_0 = y_0, omega_0
sol = odeint(diff_func, z_0, x_0)
print(sol)

def diff_func_1(z, x):
    y, omega = z

    dy_dt = omega
    domega_dt = ( (4*x**2 +  1/2)*y - x*omega ) / x**2

    return dy_dt, domega_dt

y_0 = sol[-1, 0]
omega_0 = sol[-1, -1]
z_0 = y_0, omega_0
sol_1 = odeint(diff_func_1, z_0, x_1)

plt.plot(x_0, sol[:, 1], "b", label="dy/dx(t)")
plt.plot(x_1, sol_1[:, 1], "b")
plt.legend()
plt.savefig("extratask4.png")

