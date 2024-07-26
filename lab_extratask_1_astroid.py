from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

def astr(t):
    x0 = 10 * (np.cos(t)**3)
    y0 = 10 * (np.sin(t)**3)
    phi = np.arange(0, 2*np.pi, 0.5)
    x = x0 + 0.01*np.cos(phi)
    y = y0 + 0.01*np.cos(phi)
    return x, y

def line_astr(t):
    t = np.arange(-5*np.pi, t, 0.01)
    x = 10 * (np.cos(t)**3)
    y = 10 * (np.sin(t)**3)
    return x, y

def animate(i):
    line_astroid.set_data(line_astr(t=i))
    astroid.set_data(astr(t=i))



fig, ax = plt.subplots()
line_astroid, = plt.plot( [], [], '-', color='g', label='Butterfly')
astroid, = plt.plot( [], [], 'o', color='r', label='Butterfly', lw="0.5")

edge = 20
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
    

ani = FuncAnimation(fig, animate, frames=np.arange(-5*np.pi, 5*np.pi, 0.1), interval=100)

ani.save("animation_astroid.gif")