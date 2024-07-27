# from matplotlib.animation import FuncAnimation
# import matplotlib.pyplot as plt
# import numpy as np

# def str_str(t):
#     x = np.arange(-2*5, 2*5, 0.1)
#     y = np.arange(-2*5, 2*5, 0.1)

#     # Переход к неявнозаданным координатам
#     X, Y = np.meshgrid(x, y)

#     fxy = abs(X+Y) + abs(Y-X) - 5 # Уравнеxние окружности
#     x_data = X*np.cos(t)
#     y_data = Y*np.sin(t)
#     # Команда рисования
#     plt.contour(X, Y, fxy, levels=[0])
#     return x_data, y_data

# def animate(i):
#     star.set_data(str_str(t=i))


# fig, ax = plt.subplots()

# star, = plt.plot( [], [], '-', color='r', label='Butterfly', lw="0.5")

# edge = 10
# plt.axis('equal')
# ax.set_xlim(-edge, edge)
# ax.set_ylim(-edge, edge)
    

# ani = FuncAnimation(fig, animate, frames=np.arange(0, 2*np.pi, 0.1), interval=100)

# ani.save("animation_square.gif")