import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Определяем переменную величину
x = np.arange(1, 3, 0.01)

# Определяем функцию для системы дифю уравнений
def diff_func(z, x): # z - изменяемая величина для системы
    y, omega = z # Укаханные изменения функций, через z

    # Первое уравнение системы
    dy_dx = omega
    # Второе уравнение системы
    domega_dx = np.sin(y)*omega - 3*x*y - 5

    return dy_dx, domega_dx

# Определяем начальные значения и параметры,
# входящие в систему диф. уравнений
y0 = 0.01
omega0 = 0.05

z0 = y0, omega0

sol = odeint(diff_func, z0, x)

plt.plot(x, sol[:, 0], "b", label="y(t)")
plt.plot(x, sol[:, 1], "g", label="omaga(t)")


plt.legend()
plt.savefig("fig_2.png")

