from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

def bttrfl(t):
    x = np.sin(t) * ((np.e**np.cos(t)) - (2*np.cos(4*t)) + (np.sin(t/12)**5))
    y = np.cos(t) * ((np.e**np.cos(t)) - (2*np.cos(4*t)) + (np.sin(t/12)**5))
    return x, y

def animate(t):
    butterfly.set_data(bttrfl(t=t))

if __name__ == "__main__":

    fig, ax = plt.subplots()
    butterfly, = plt.plot([], [], '-', color='r', label='Butterfly')

    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    

    ani = FuncAnimation(fig, animate, frames=np.arange(0, 12.1*np.pi, 0.1), interval=100)

    ani.save('animation_butterfly.gif')
    