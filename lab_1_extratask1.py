import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

r_0 = 384400000 # высота, м
v_0 = 1

R_earth = 6378.1 * 10**3 # радиус Земли, м
M_earth = 5.974 * 10**24 # масса Земли, кг
G = 6.67 * 10**(-11)

r = np.arange(0, r_0 - R_earth, 500)

def speed_function(v, r):
    dvdr = (G*M_earth)/(v*(r_0 + R_earth - r)**2)

    return dvdr

v_r = odeint(speed_function, v_0, r)


plt.plot(r_0 - r, v_r[:,0], label="скорость")
plt.xlabel("Время, секунды")
plt.ylabel("Функция скорости")
plt.title("Закон изменения скорости")
plt.legend()

plt.savefig("lab_extratask1.png")