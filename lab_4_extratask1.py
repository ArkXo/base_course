import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def func(r, N, v, x_0, y_0):
    X = np.array([])
    Y = np.array([])
    for i in range(0, N+1):
        x = r * np.cos(2*np.pi*i/N) + x_0
        y = r * np.sin(2*np.pi*i/N) + y_0
        X = np.append(X, [x])
        Y = np.append(Y, [y])

    return X, Y

sol = func(5, 10, 2, 3, 4)
t = sol[0]
s = sol[1]
print(t)

plt.plot(t, s, label="Площадь")
plt.savefig("lab_extratask1.png")