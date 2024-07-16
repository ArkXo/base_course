import numpy as np
import matplotlib.pyplot as plt

def astroid(R):
    t = np.arange(-5*np.pi, 5*np.pi, 0.1)  # Параметр

    x = R * (np.cos(t)**3)
    y = R * (np.sin(t)**3)

    plt.plot(x, y, ls='-', lw=3)
    plt.savefig('fig_astroid.png')

astroid(int(input("Введите значение радиуса: ")))