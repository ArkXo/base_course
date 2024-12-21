import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def func(r, N, v, x_0, y_0):
    X = np.array([])
    Y = np.array([])
    for i in range(0, N+1):
        x = r * np.cos(360*i/N) + x_0
        y = r * np.cos(360*i/N) + y_0
        X = np.append(X, [x])
        Y = np.append(Y, [y])

    return X, Y

sol = func(5, 100, 2, 3, 4)
x = sol[0]
print(x)