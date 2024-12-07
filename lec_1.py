import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
	
frames = 500
seconds_in_year = 365 * 24 * 60 * 60
years = 1
t = np.linspace(0, years*seconds_in_year, frames)

def move_func(s, t):
    x, vx, y, vy = s

    dx_dt = vx
    dvx_dt = - G * M * x / (x**2 + y**2)**1.5
    dy_dt = vy
    dvy_dt = - G * M * y / (x**2 + y**2)**1.5

    return dx_dt, dvx_dt, dy_dt, dvy_dt

G = 6.67 * 10**(-11)
M = 1.989 * 10**30

x0 = 149.6 * 10**9
vx0 = 0
y0 = 0
vy0 = 30000

s0 = x0, vx0, y0, vy0

sol = odeint(move_func, s0, t)
x = sol[:, 0]
y = sol[:, 2]

def animate(i):
    ball.set_data([x[i]], [y[i]])

    ball_line.set_data([x[:i]], [y[:i]])

fig, ax = plt.subplots()

ball, = plt.plot([], [], 'o', color='b')
ball_line, = plt.plot([], [], '-', color='b')
plt.plot([0], [0], 'o', color='y', ms=20)

plt.axis("equal")
edge = 2 * x0
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani = FuncAnimation(fig, animate, frames=frames, interval=30)
ani.save("earth_sun.gif")