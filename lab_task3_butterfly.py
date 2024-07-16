from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

def bttrfl(t):
    x = np.sin(t)
    y = np.cos(t)
    return x, y

def animate(t):
    butterfly.set_data(bttrfl(t=t))

if __name__ == "__main__":

    fig, ax = plt.subplots()
    butterfly, = plt.plot([], [], '-', color='r', label='Butterfly')

    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    

    ani = FuncAnimation(fig, animate, frames=np.linspace(0, 2*np.pi, 100), interval=100)

    ani.save("animation_butterfly.gif")
    