import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

S_0 = 0.16
E_0 = 1360
k = 340 * 10**(-8)

t = np.arange(0, 24, 0.01)


def func_victoria_rega(S, t):
    print(t)
    if t >= 6 and t <= 18:
        dsdt = k * E_0*np.cos((12-t)*np.pi/12)*np.sqrt((S**3)/np.pi)
    else:
        dsdt = 0
    return dsdt

S_t = odeint(func_victoria_rega, S_0, t)

plt.plot(t, S_t, label="Площадь")
plt.xlabel("Время, секунды")
plt.ylabel("Функция скорости")
plt.title("Закон изменения скорости")
plt.legend()

plt.savefig("lab_extratask2.png")
