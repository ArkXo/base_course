from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

def str_str(t):
    j = np.arange(0, 4*np.pi, 0.1)
    x = 12 * np.cos(j) + 8 * np.cos(1.5 * j)
    y = 12 * np.sin(j) - 8 * np.sin(1.5 * j)
    X = x * np.cos(t) - y * np.sin(t)
    Y = y * np.cos(t) + x * np.sin(t)
    return X, Y



def animate(i):
    star.set_data(str_str(t=i))



fig, ax = plt.subplots()
star, = plt.plot( [], [], '-', color='r', label='Butterfly', lw="0.5")

edge = 25
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
    

ani = FuncAnimation(fig, animate, frames=np.arange(0, 4*np.pi, 0.1), interval=100)

ani.save("animation_star.gif")