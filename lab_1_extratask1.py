import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

h_0 = 1000 * 10**3 # высота, м
R_earth = 6378.1 * 10**3 # радиус Земли, м
M_earth = 5.974 * 10**24 # масса Земли, кг
G = 6.67 * 10**(-11)
t = np.arange(0, 50, 1)

def speed_function(h, t):
    dvdt = G*M_earth/(R_earth+h)**2
    print(dvdt)
    return dvdt

v_t = odeint(speed_function, h_0, t)


plt.plot(t, v_t[:,0], label="скорость")
plt.xlabel("Время, секунды")
plt.ylabel("Функция скорости")
plt.title("Закон изменения скорости")
plt.legend()

plt.savefig("lab_extratask1.png")