import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

n_0 = 1000
k = 0.08
t_0 = 4*365
t = np.arange(0, t_0, 1)

print("Закон изменения инвестиций: v = 0.08 * n,\nгде v - скорость, n - кол-во бактерий в моменте, k - коэфицент пропорциональности.")
print()

def bacterium_function(n, t):
    dndt = -k * n
    return dndt

n_t = odeint(bacterium_function, n_0, t)

print(f"Время, спустя которое бактерий станет в  раз больше", n_t[-1])


plt.plot(t, n_t[:,0], label="Размножение бактерий")
plt.xlabel("Время увеличения, секунды")
plt.ylabel("Функция увеличения")
plt.title("Закон увеличения")
plt.legend()

plt.savefig("fig_2.png")