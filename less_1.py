import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 200
t = np.linspace(0, 5, frames)
print(len(t))

def move_func(z, t):
    x, vx, y, vy = z
    
    dx_dt = vx
    dvx_dt = 0
    dy_dt = vy
    dvy_dt = - g
    
    return dx_dt, dvx_dt, dy_dt, dvy_dt


g = 9.8
v = 15
alpha = 80 * np.pi / 180

x0 = 0
vx0 = v * np.cos(alpha)
y0 = 0
vy0 = v * np.sin(alpha)

z0 = x0, vx0, y0, vy0

sol = odeint(move_func, z0, t)


def solve_func(i, key):
    if key == 'point':
        x = sol[i, 0]
        y = sol[i, 2]
    else:
        x = sol[:i, 0]
        y = sol[:i, 2]
    return x, y

def animate(i):
    print(i)
    ball.set_data(solve_func(i, 'point'))
    # ball_line.set_data(solve_func(i, 'line'))

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='r')
# ball_line, = plt.plot([], [], '-', color='r')

edge = 15
ax.set_xlim(0, edge)
ax.set_ylim(0, edge)

ani = FuncAnimation(fig, animate, frames=200, interval=30)

ani.save('animation.gif')