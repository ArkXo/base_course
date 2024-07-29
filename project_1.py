from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

# Справочные данные:
G = 6.67 * 10**(-11)
mass_son = 1.989 * 10**30
# Марс:
a_mars = 1.52
T_mars = 686.98
# Юпитер:
a_jupiter = 5.2
T_jupiter = 11.862 * 365.256
# Сатурн:
a_saturn = 9.54
T_saturn = 29.458 * 365.256
# Уран:
a_uranus = 19.19
T_uranus = 84.01 * 365.256
# Нептун:
a_neptune = 30
T_neptune = 164.79 * 365.256

# Угловая скорость Земли:
angle_vel_earth = 0.9856 # градус в день

# Данные выбранной планеты:
name_planet = input("Введите название планеты к которой отправили корабль(с маленькой буквы): ")

if name_planet == "марс":
    a_planet = a_mars
    T_planet = T_mars
    angle_vel_planet = 360 / T_planet # градус в день
elif name_planet == "юпитер":
    a_planet = a_jupiter
    T_planet = T_jupiter
    angle_vel_planet = 360 / T_planet # градус в день
elif name_planet == "сатурн":
    a_planet = a_saturn
    T_planet = T_saturn
    angle_vel_planet = 360 / T_planet # градус в день
elif name_planet == "уран":
    a_planet = a_uranus
    T_planet = T_uranus
    angle_vel_planet = 360 / T_planet # градус в день
elif name_planet == "нептун":
    a_planet = a_neptune
    T_planet = T_neptune
    angle_vel_planet = 360 / T_planet # градус в день

# Данные для угловой скорости космического корабля:
a = (1+a_planet)/2
e = (a_planet-1)/(a_planet+1)
b = a * (1 - e**2)**(1/2)
T = ( (4 * np.pi**2) / (G * mass_son) * (a * 149.6 * 10**9)**3)**(1/2) / (60*60*24)
print(f"Время полёта займёт: {T/2} дней")

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

# Движение планеты:

def move_planet(time):

    alpha = angle_vel_planet * np.pi / 180 * time + np.pi - angle_vel_planet * np.pi / 180 * T /2

    x0 = a_planet * np.cos(alpha)
    y0 = a_planet * np.sin(alpha)

    phi = np.arange(0, 2*np.pi, 0.5)

    x = x0 + 0.01*np.cos(phi)
    y = y0 + 0.01*np.sin(phi)

    return x, y

def move_planet_line(time):

    alpha = angle_vel_planet * np.pi / 180 * time + np.pi - angle_vel_planet * np.pi / 180 * T /2
    alpha = np.arange(0, alpha, 0.01)

    x = a_planet * np.cos(alpha)
    y = a_planet * np.sin(alpha)

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

    # Движение планеты:
    planet_line.set_data(move_planet_line(time=i))
    planet.set_data(move_planet(time=i))

    # Движение космического коробля:
    spaceship_line.set_data(move_spaceship_line(time=i))
    spaceship.set_data(move_spaceship(time=i))

fig, ax = plt.subplots()

# Земля:
earth_line, = plt.plot( [], [], '-', color='g')
earth, = plt.plot( [], [], 'o', color='b', lw="0.5")

# Планета:
planet_line, = plt.plot( [], [], '-', color='g')
planet, = plt.plot( [], [], 'o', color='orange', lw="0.5")

# Космический корабль:
spaceship_line, = plt.plot( [], [], '-', color='g')
spaceship, = plt.plot( [], [], 'o', color='r', lw="0.5")

edge = a_planet*1.1
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
plt.axis('scaled')

ani = FuncAnimation(fig, animate, frames=np.arange(0, T/2, int(input("Введите сколько дней проходит между кадрами: "))), interval=0.01)

ani.save("project_1.gif")