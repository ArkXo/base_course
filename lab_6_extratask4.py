import matplotlib.pyplot as plt
import numpy as np

def steps(n):
    x = np.arange(0, 3+2, 1)
    new_x = np.array([])
    y = np.array([])
    for i in range(0, 4):
        new_x = np.append(new_x, [x[i], x[i]])
        y = np.append(y, [x[i], x[i]])
    new_x = np.delete(new_x, 0)
    y = np.delete(y, -1)
    print(new_x)

    plt.plot(new_x, y, label="Ступеньки")
    plt.xlabel("Coord - x")
    plt.ylabel("Coord - y")
    plt.title("Refund")
    plt.legend()
    plt.grid()
    plt.axis('equal')
    
    plt.savefig('fig_extratask4.png')

steps(int(input("Введите значение количества ступенек: ")))

# x = np.arange(0, 3+2, 1)
# print(x)