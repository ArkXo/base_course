# import numpy as np
# from scipy.integrate import odeint
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# # Определяем переменную величину
# frames = 200
# t = np.linspace(0, 5, frames)

# # Определяем функцию для системы диф. уравнений
# def move_func(z, t):
#     x, vx, y, vy = z
    
#     dx_dt = vx
#     dvx_dt = 0
#     dy_dt = vy
#     dvy_dt = - g
    
#     return dx_dt, dvx_dt, dy_dt, dvy_dt

# # Определяем начальные значения и параметры
# g = 9.8
# v = 15
# alpha = 80 * np.pi / 180

# x0 = 0
# vx0 = v * np.cos(alpha)
# y0 = 0
# vy0 = v * np.sin(alpha)

# z0 = x0, vx0, y0, vy0

# sol = odeint(move_func, z0, t)

  
# # Строим решение в виде графика и анимируем
# fig, ax = plt.subplots()

# ball = plt.plot(sol[:, 0], sol[:, 2], 'o', color='r')[0]
# ball_line = plt.plot(sol[:, 0], sol[:, 2], '-', color='r')[0]


# def animate(i):
#     ball.set_xdata(sol[i, 0])
#     ball.set_ydata(sol[i, 2])

#     ball_line.set_xdata(sol[:i, 0])
#     ball_line.set_ydata(sol[:i, 2])


# animate(1)
# # ani = FuncAnimation(fig, animate, frames=frames, interval=30)

# # edge = 15
# # ax.set_xlim(0, edge)
# # ax.set_ylim(0, edge)

# # ani.save('animation.gif')

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.animation as animation

fig, ax = plt.subplots()
t = np.linspace(0, 3, 40)
g = -9.81
v0 = 12
z = g * t**2 / 2 + v0 * t

v02 = 5
z2 = g * t**2 / 2 + v02 * t

scat = ax.scatter(t[0], z[0], c="b", s=5, label=f'v0 = {v0} m/s')
line2 = ax.plot(t[0], z2[0], label=f'v0 = {v02} m/s')[0]
ax.set(xlim=[0, 3], ylim=[-4, 10], xlabel='Time [s]', ylabel='Z [m]')
ax.legend()


def update(frame):
    # for each frame, update the data stored on each artist.
    x = t[:frame]
    y = z[:frame]
    # update the scatter plot:
    data = np.stack([x, y]).T
    scat.set_offsets(data)
    # update the line plot:
    line2.set_xdata(t[:frame])
    line2.set_ydata(z2[:frame])
    return (scat, line2)


ani = animation.FuncAnimation(fig=fig, func=update, frames=40, interval=30)
ani.save('animation.gif')
