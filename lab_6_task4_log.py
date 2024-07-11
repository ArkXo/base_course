import matplotlib.pyplot as plt
import numpy as np

def log(b):
    phi = np.arange(0, 8*(np.pi), 0.1)
    r = ((np.e)**(b*phi))
    x = r * np.cos(phi)
    y = r * np.sin(phi)

    plt.plot(x, y, label="Логарифмическая спираль")
    plt.xlabel("Coord - x")
    plt.ylabel("Coord - y")
    plt.title("Логарифмическая спираль")
    plt.legend()
    plt.grid()
    plt.axis('equal')
    
    plt.savefig('fig_task4_log.png')

log(float(input("Введите значение b: ")))