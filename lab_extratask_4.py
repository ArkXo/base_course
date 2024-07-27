from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

def str_str(t, a =5):

    x = np.arange(-a, a, 0.1)
    y = np.arange(-a, a, 0.1)

    X, Y = np.meshgrid(x, y)


    x_data = X * np.cos(t) - Y * np.sin(t)
    y_data = Y * np.cos(t) + X * np.sin(t)

    return x_data, y_data

def animate(i):
    star.set_data(str_str(t=i))

fig, ax = plt.subplots()
star, = plt.plot( [], [], '-', color='r', label='Butterfly', lw="0.5")

edge = 10
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani = FuncAnimation(fig, animate, frames=np.arange(0, 2*np.pi, 0.1), interval=100)

ani.save("animation_square.gif")