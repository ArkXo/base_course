from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np


# Угловая скорость Земли:
angle_vel_earth = 0.9856 # градус в день

# Угловая скорость Юпитера:
angle_vel_jupiter = 0.083 # градус в день

# Данные для угловой скорости космического корабля:
a = 3.1
b = 2.28
T = 1994
e = 0.677

# Движение Земли:

def move_earth(time):

    alpha = angle_vel_earth * np.pi / 180 * time

    x0 = 1 * np.cos(alpha)
    y0 = 1 * np.sin(alpha)

    phi = np.arange(0, 2*np.pi, 0.5)

    x = x0 + 0.01*np.cos(phi)
    y = y0 + 0.01*np.sin(phi)

    return x, y

def move_earth_line(time):

    alpha = angle_vel_earth * np.pi / 180 * time
    alpha = np.arange(0, alpha, 0.01)

    x = 1 * np.cos(alpha)
    y = 1 * np.sin(alpha)

    return x, y

# Движение Юпитера:

def move_jupiter(time):

    alpha = angle_vel_jupiter * np.pi / 180 * time + np.pi - angle_vel_jupiter * np.pi / 180 * T /2

    x0 = 5.2 * np.cos(alpha)
    y0 = 5.2 * np.sin(alpha)

    phi = np.arange(0, 2*np.pi, 0.5)

    x = x0 + 0.01*np.cos(phi)
    y = y0 + 0.01*np.sin(phi)

    return x, y

def move_jupiter_line(time):

    alpha = angle_vel_jupiter * np.pi / 180 * time + np.pi - angle_vel_jupiter * np.pi / 180 * T /2
    alpha = np.arange(0, alpha, 0.01)

    x = 5.2 * np.cos(alpha)
    y = 5.2 * np.sin(alpha)

    return x, y

# Движение космического коробля:

def move_spaceship(time):

    M = 2 * np.pi * time / T

    for j in np.arange(0, 3*np.pi, 0.0001):
        fxy = j - e * np.sin(j) - M
        if fxy >=0.01:
            E = j
            break

    x0 = a * np.cos(E) - (a-1)
    y0 = b * np.sin(E)

    phi = np.arange(0, 2*np.pi, 0.5)

    x = x0 + 0.01*np.cos(phi)
    y = y0 + 0.01*np.sin(phi)
    return x, y

def move_spaceship_line(time):

    M = 2 * np.pi * time / T

    for j in np.arange(0, 3*np.pi, 0.0001):
        fxy = j - e * np.sin(j) - M
        if fxy >=0.01:
            E = j
            break

    E = np.arange(0, E, 0.01)
    x = a * np.cos(E) - (a-1)
    y = b * np.sin(E)

    return x, y

# Анимация:
def animate(i):

    # Движение Земли:
    earth_line.set_data(move_earth_line(time=i))
    earth.set_data(move_earth(time=i))

    # Движение Юпитера:
    jupiter_line.set_data(move_jupiter_line(time=i))
    jupiter.set_data(move_jupiter(time=i))

    # Движение космического коробля:
    spaceship_line.set_data(move_spaceship_line(time=i))
    spaceship.set_data(move_spaceship(time=i))



fig, ax = plt.subplots()

# Земля:
earth_line, = plt.plot( [], [], '-', color='g')
earth, = plt.plot( [], [], 'o', color='b', lw="0.5")

# Юпитер:
jupiter_line, = plt.plot( [], [], '-', color='g')
jupiter, = plt.plot( [], [], 'o', color='orange', lw="0.5")

# Космический корабль:
spaceship_line, = plt.plot( [], [], '-', color='g')
spaceship, = plt.plot( [], [], 'o', color='r', lw="0.5")

edge = 6
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
plt.axis('scaled')

ani = FuncAnimation(fig, animate, frames=np.arange(0, 1000, 3), interval=0.01)

ani.save("project.gif")