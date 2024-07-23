from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

def frctl(n):
    x = [0]
    y = [0]
    C = 0.3
    D = 0.33
    for i in range(0, n-1):
        x.append( x[-1]**2 - y[-1]**2 + C )
        y.append( 2 * x[-1] * y[-1] + D )
        ax.set_xlim((x[-1])-0.01/(i+10000*(i+1)), x[-1]+0.01/(i+10000*(i+1)))
        ax.set_ylim((y[-1])-0.01/(i+10000*(i+1)), y[-1]+0.01/(i+10000*(i+1)))
    return x, y


def animate(w):
    fractal.set_data(frctl(n=w))



fig, ax = plt.subplots()
fractal, = plt.plot([], [], '-', color='r', label='Butterfly', lw = 1)


ani = FuncAnimation(fig, animate, frames=np.arange(0, int(input()), 1), interval=100)

ani.save("animation_task4.gif")
