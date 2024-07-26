from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
x = []
y = []

def bttrfl(t):
    x.append = 5 * (np.cos(t)**3)
    y.append = 5 * (np.sin(t)**3)
    return x, y


def animate(i):
    butterfly.set_data(bttrfl(t=i))



fig, ax = plt.subplots()
butterfly, = plt.plot( [], [], 'o', color='r', label='Butterfly')

edge = 20
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
    

ani = FuncAnimation(fig, animate, frames=np.arange(-5*np.pi, 5*np.pi, 0.1), interval=100)

ani.save("animation_heart.gif")