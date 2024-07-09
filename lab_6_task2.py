import matplotlib.pyplot as plt
import numpy as np

def hyper(minimum, maximum, N):
    x = np.linspace(0, maximum, N)
    y = 20/x
    plt.plot(x, y, label="my hyperbola")

    x = np.linspace(minimum, 0, N)
    y = 20/x
    plt.plot(x, y, label="my hyperbola")

    plt.xlabel("Coord - x")
    plt.ylabel("Coord - y")
    plt.title("Parabola")
    plt.legend()
    
    plt.savefig('fig_3.png')

hyper(int(input("Введите значение минимума х: ")), int(input("Введите значение максимума х: ")), int(input("Введите значение N: ")))
