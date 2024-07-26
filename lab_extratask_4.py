from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

def str_str(t):
    x = np.arange(-2*5, 2*5, 0.1)
    y = np.arange(-2*5, 2*5, 0.1)

    # Переход к неявнозаданным координатам
    X, Y = np.meshgrid(x, y)

    fxy = abs(X+Y)*np.cos(t) + abs(Y-X)*np.sin(t) # Уравнение окружности

    # Команда рисования
    plt.contour(X, Y, fxy, levels=[0])
    return X, Y




fig, ax = plt.subplots()

plt.axis('equal')
    

ani = FuncAnimation(fig, str_str, frames=np.arange(0, 2*np.pi, 0.1), interval=100)

ani.save("animation_square.gif")