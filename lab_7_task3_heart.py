from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

def bttrfl(i):
    t = np.arange(0, i, 0.01)
    x = 16 * (np.sin(t)**3)
    y = 13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)
    return x, y


def animate(i):
    butterfly.set_data(bttrfl(i=i))



fig, ax = plt.subplots()
butterfly, = plt.plot([], [], '-', color='r', label='Butterfly')

edge = 20
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
    

ani = FuncAnimation(fig, animate, frames=np.arange(0, 2*np.pi, 0.1), interval=100)

ani.save("animation_heart.gif")