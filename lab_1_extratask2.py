import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

S_0 = 0.16
E_0 = 1360
k = 0.00005
S =[]

t = np.arange(0, 24, 0.1)

for i in np.arange(0, 24, 0.1):
    if i >= 6 and i <= 18:
        alpha = abs(12-i)*15 * np.pi/180
        dSdt = k * E_0*np.cos(alpha)*np.sqrt((S_0**3)/np.pi)
    else:
        dSdt = 0
    S_0 += dSdt
    S.append(S_0)
    if i == 12:
        k = 0.25/(S_0)*k
        print(k)

S_0 = 0.16

def func_victoria_rega(S, t):
    print(t)
    if t >= 6 and t <= 18:
        alpha = abs(12-t)*15 * np.pi/180
        dsdt = k * E_0*np.cos(alpha)*np.sqrt((S**3)/np.pi)
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
