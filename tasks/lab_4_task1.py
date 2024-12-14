	
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
 
# Определяем переменную величину
frames = 500
seconds_in_year = 365 * 24 * 60 * 60
years = 1
t = np.linspace(0, years*seconds_in_year, frames)

G = 6.67 * 10**(-11)
M = 1.98 * 10**(30)
ae = 149 * 10**9
v_earth = 30000
 
s0 = ([0.387*ae, 0, 0, v_earth/np.sqrt(0.387)],
      [0.723*ae, 0, 0, v_earth/np.sqrt(0.723)],
      [1*ae, 0, 0, v_earth],
      [1.52*ae, 0, 0, v_earth/np.sqrt(1.52)])

def move_func(s, t):
    x, v_x, y, v_y = s
 
    dx_dt = v_x
    dvx_dt = - G * M * x / (x**2 + y**2)**1.5
    dy_dt = v_y
    dvy_dt = - G * M * y / (x**2 + y**2)**1.5

    return dx_dt, dvx_dt, dy_dt, dvy_dt

anim = []
fig, ax = plt.subplots()
plt.axis("equal")
edge = 2
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

plt.plot([0], [0], 'o', color='y', ms=20)

for j in s0:

    sol = odeint(move_func, j, t)

    x = sol[:, 0] / ae
    y = sol[:, 2] / ae

    def animate(i):
        ball.set_data([x[i]], [y[i]])

        ball_line.set_data([x[:i]], [y[:i]])

    ball, = plt.plot([], [], 'o', color='b')
    ball_line, = plt.plot([], [], '-', color='b')
    ani = FuncAnimation(fig, animate, frames=frames, interval=30)
    ani.save("gifs/task1.gif")

