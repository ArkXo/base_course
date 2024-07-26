from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

def cyc(t):
    x0 = 10 * (t - np.sin(t)**3)
    y0 = 10 * (1 - np.cos(t)**3)
    phi = np.arange(0, 2*np.pi, 0.5)
    x = x0 + 0.01*np.cos(phi)
    y = y0 + 0.01*np.cos(phi)
    return x, y

def line_cyc(t):
    j = np.arange(-2*np.pi, t, 0.01)
    x = 10 * (j - np.sin(j)**3)
    y = 10 * (1 - np.cos(j)**3)
    return x, y

def animate(i):
    line_cycloid.set_data(line_cyc(t=i))
    cycloid.set_data(cyc(t=i))



fig, ax = plt.subplots()
line_cycloid, = plt.plot( [], [], '-', color='g', label='Butterfly')
cycloid, = plt.plot( [], [], 'o', color='r', label='Butterfly', lw="0.5")

edge = 70
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
    

ani = FuncAnimation(fig, animate, frames=np.arange(-2*np.pi, 2*np.pi, 0.1), interval=100)

ani.save("animation_cycloid.gif")