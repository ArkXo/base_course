from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np


# Угловая скорость Земли:
angle_vel_earth = 0.9856 # градус в день

# Угловая скорость Юпитера:
angle_vel_jupiter = 0.083 # градус в день

# Данные для гловой скорости космического корабля:
G = 6.67 * 10**(-11)
mass_son = 1.989 * 10**30
a = 3.1
e = 0.677
p = 1.677



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

    alpha = angle_vel_jupiter * np.pi / 180 * time

    x0 = 5.2 * np.cos(alpha)
    y0 = 5.2 * np.sin(alpha)

    phi = np.arange(0, 2*np.pi, 0.5)

    x = x0 + 0.01*np.cos(phi)
    y = y0 + 0.01*np.sin(phi)

    return x, y

def move_jupiter_line(time):

    alpha = angle_vel_jupiter * np.pi / 180 * time
    alpha = np.arange(0, alpha, 0.01)

    x = 5.2 * np.cos(alpha)
    y = 5.2 * np.sin(alpha)

    return x, y

# Движение космического коробля:

def move_spaceship(time):

    r = p / (1-e*np.cos(alpha))
    angle_vel = np.sqrt(mass_son*G) * np.sqrt( (2*a-r) / ((r**3) * a))
    alpha = angle_vel * np.pi / 180 * time
    

    x0 = 5.2 * np.cos(alpha)
    y0 = 5.2 * np.sin(alpha)

    phi = np.arange(0, 2*np.pi, 0.5)

    x = x0 + 0.01*np.cos(phi)
    y = y0 + 0.01*np.sin(phi)

    return x, y

def move_spaceship_line(time):

    alpha = angle_vel_jupiter * np.pi / 180 * time
    alpha = np.arange(0, alpha, 0.01)

    x = 5.2 * np.cos(alpha)
    y = 5.2 * np.sin(alpha)

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
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani = FuncAnimation(fig, animate, frames=np.arange(0, 365, 5), interval=0.01)

ani.save("project.gif")