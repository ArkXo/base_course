from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

def bttrfl(t):
    x = np.sin(t) * ((np.e**np.cos(t)) - (2*np.cos(4*t)) + (np.sin(t/12)**5))
    y = np.cos(t) * ((np.e**np.cos(t)) - (2*np.cos(4*t)) + (np.sin(t/12)**5))
    return x, y


def animate(i):
    butterfly.set_data(bttrfl(t=i))



fig, ax = plt.subplots()
butterfly, = plt.plot([], [], '-', color='r', label='Butterfly')

edge = 5
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
    

ani = FuncAnimation(fig, animate, frames=12*np.pi, interval=100)

ani.save("animation_butterfly.gif")