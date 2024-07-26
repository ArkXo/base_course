from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

def sin_1(t):
    x0 = t
    y0 = 3 * np.sin(2*t)
    phi = np.arange(0, 2*np.pi, 0.5)
    x = x0 + 0.01*np.cos(phi)
    y = y0 + 0.01*np.cos(phi)
    return x, y

def line_sin_1(t):
    t = np.arange(0, t, 0.01)
    x = t
    y = 3 * np.sin(2*t)
    return x, y

def sin_2(t):
    x0 = t
    y0 = 2 * np.sin(3*t)
    phi = np.arange(0, 2*np.pi, 0.5)
    x = x0 + 0.01*np.cos(phi)
    y = y0 + 0.01*np.cos(phi)
    return x, y

def line_sin_2(t):
    t = np.arange(0, t, 0.01)
    x = t
    y = 2 * np.sin(3*t)
    return x, y


def animate(i):
    line_asinus_1.set_data(line_sin_1(t=i))
    sinus_1.set_data(sin_1(t=i))
    line_asinus_2.set_data(line_sin_2(t=i))
    sinus_2.set_data(sin_2(t=i))



fig, ax = plt.subplots()

line_asinus_1, = plt.plot( [], [], '-', color='g', label='Butterfly')
sinus_1, = plt.plot( [], [], 'o', color='r', label='Butterfly', lw="0.5")

line_asinus_2, = plt.plot( [], [], '-', color='b', label='Butterfly')
sinus_2, = plt.plot( [], [], 'o', color='y', label='Butterfly', lw="0.5")

ax.set_xlim(-np.pi, 10*np.pi)
ax.set_ylim(-4, 4)
    

ani = FuncAnimation(fig, animate, frames=np.arange(0, 10*np.pi, 0.1), interval=100)

ani.save("animation_extratask2.gif")