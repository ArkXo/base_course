import numpy as np
import matplotlib.pyplot as plt

def cycloid(R):
    t = np.arange(-2*np.pi, 2*np.pi, 0.1)  # Параметр

    x = R * (t - np.sin(t)**3)
    y = R * (1 - np.cos(t)**3)

    plt.plot(x, y, ls='-', lw=3)
    plt.savefig('fig_cycloid.png')

cycloid(int(input("Введите значение радиуса: ")))