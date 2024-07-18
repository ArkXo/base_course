from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

def bttrfl(i):
    t = np.arange(i- (2*np.pi), i, 0.01)
    x = np.sin(t) * ((np.e**np.cos(t)) - (2*np.cos(4*t)) + (np.sin(t/12)**5))
    y = np.cos(t) * ((np.e**np.cos(t)) - (2*np.cos(4*t)) + (np.sin(t/12)**5))
    return x, y


def animate(i):
    butterfly.set_data(bttrfl(i=i))



fig, ax = plt.subplots()
butterfly, = plt.plot([], [], '-', color='r', label='Butterfly')

edge = 5
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
    

ani = FuncAnimation(fig, animate, frames=np.arange(0, 12.1*np.pi, np.pi/2), interval=200)

ani.save("animation_butterfly.gif")