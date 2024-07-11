import matplotlib.pyplot as plt
import numpy as np

def refund(a, b):
    x = np.linspace(-20, 20, 100)
    y = np.array([1])

    for i in range(0, 100):
        if x[i] < a:
            y = np.append(y, a**2)
        elif a<= x[i] and x[i] <= b:
            y = np.append(y, x[i]**2)
        elif x[i] > b:
            y = np.append(y, b**2)
    y = np.delete(y, 0)

    plt.plot(x, y, label="Refund")
    plt.xlabel("Coord - x")
    plt.ylabel("Coord - y")
    plt.title("Refund")
    plt.legend()
    plt.grid()
    plt.axis('equal')
    
    plt.savefig('fig_extratask3.png')

refund(int(input("Введите значение a: ")), int(input("Введите значение b: ")))
