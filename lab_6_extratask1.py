import matplotlib.pyplot as plt
import numpy as np

def lis(lim, B, b):
    delta = np.pi/2
    t = np.arange(-lim, lim, 0.1)
    x = np.sin(t + delta)
    y = B * np.sin(b * t)

    plt.plot(x, y, label="Кривая Лиссажу")
    plt.xlabel("Coord - x")
    plt.ylabel("Coord - y")
    plt.title("Кривая Лиссажу")
    plt.legend()
    plt.grid()
    plt.axis('equal')
    
    plt.savefig('fig_extratask1.png')

lis(int(input("Введите значение предела t: ")), float(input("Введите значение B: ")), float(input("Введите значение b: ")))