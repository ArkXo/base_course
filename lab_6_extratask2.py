import matplotlib.pyplot as plt
import numpy as np

def spiral(p, e):
    phi = np.arange(0, 2*(np.pi), 0.01)
    r = p / (1 + e * np.cos(phi))
    x = r * np.cos(phi)
    y = r * np.sin(phi)

    plt.plot(x, y, label="Эллипс")
    plt.xlabel("Coord - x")
    plt.ylabel("Coord - y")
    plt.title("Эллипс")
    plt.legend()
    plt.grid()
    plt.axis('equal')
    
    plt.savefig('fig_extratask2.png')

spiral(float(input("Введите значение фокального параметра: ")), float(input("Введите значение эксцентриситета: ")))