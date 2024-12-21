import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
 
# Определяем переменную величину
frames = 500
seconds_in_year = 365 * 24 * 60 * 60
years = 1
t = np.linspace(0, years*seconds_in_year, frames)

k = 9 * 10**9
Q = 15
ae = 10**9
v = 29000
 
s0_1 = 0.387*ae, -v/np.sqrt(0.387), 0, 0, 3, 1
s0_2 = 0.723*ae, -v/np.sqrt(0.723), 0, 0, 4, 2
s0_3 = 1*ae, -v, 0, 0, 6, 2
s0_4 = 1.52*ae, -v/np.sqrt(1.52), 0, 0, -5, 3
s0_5 = 2*ae, -v/np.sqrt(2), 0, 0, -3, 1
s0_6 = 2.57*ae, -v/np.sqrt(2.57), 0, 0, -6, 2

def move_func(s, t):
    x, v_x, y, v_y, q, m = s
    dx_dt = v_x
    dvx_dt = -(k * Q * q / m) * x / (x**2 + y**2)**1.5
    dy_dt = v_y
    dvy_dt = -(k * Q * q / m) * y / (x**2 + y**2)**1.5
    dq_dt = 0
    dm_dt = 0

    return dx_dt, dvx_dt, dy_dt, dvy_dt, dq_dt, dm_dt

sol_1 = odeint(move_func, s0_1, t)
sol_2 = odeint(move_func, s0_2, t)
sol_3 = odeint(move_func, s0_3, t)
sol_4 = odeint(move_func, s0_4, t)
sol_5 = odeint(move_func, s0_5, t)
sol_6 = odeint(move_func, s0_6, t)

x_1 = sol_1[:, 0] / ae
y_1 = sol_1[:, 2] / ae

x_2 = sol_2[:, 0] / ae
y_2 = sol_2[:, 2] / ae

x_3 = sol_3[:, 0] / ae
y_3 = sol_3[:, 2] / ae

x_4 = sol_4[:, 0] / ae
y_4 = sol_4[:, 2] / ae

x_5 = sol_5[:, 0] / ae
y_5 = sol_5[:, 2] / ae

x_6 = sol_6[:, 0] / ae
y_6 = sol_6[:, 2] / ae

def animate(i):
    ball_1.set_data([x_1[i]], [y_1[i]])
    ball_1_line.set_data([x_1[:i]], [y_1[:i]])

    ball_2.set_data([x_2[i]], [y_2[i]])
    ball_2_line.set_data([x_2[:i]], [y_2[:i]])

    ball_3.set_data([x_3[i]], [y_3[i]])
    ball_3_line.set_data([x_3[:i]], [y_3[:i]])    
    
    ball_4.set_data([x_4[i]], [y_4[i]])
    ball_4_line.set_data([x_4[:i]], [y_4[:i]])

    ball_5.set_data([x_5[i]], [y_5[i]])
    ball_5_line.set_data([x_5[:i]], [y_5[:i]])

    ball_6.set_data([x_6[i]], [y_6[i]])
    ball_6_line.set_data([x_6[:i]], [y_6[:i]])

fig, ax = plt.subplots()
plt.axis("equal")
edge = 10
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

plt.plot([0], [0], 'o', color='y', ms=20)

ball_1_line, = plt.plot([], [], '-', color='0')
ball_1, = plt.plot([], [], 'o', color='m')

ball_2_line, = plt.plot([], [], '-', color='0')
ball_2, = plt.plot([], [], 'o', color='g')

ball_3_line, = plt.plot([], [], '-', color='0')
ball_3, = plt.plot([], [], 'o', color='b')

ball_4_line, = plt.plot([], [], '-', color='0')
ball_4, = plt.plot([], [], 'o', color='r')

ball_5_line, = plt.plot([], [], '-', color='0')
ball_5, = plt.plot([], [], 'o', color='r')

ball_6_line, = plt.plot([], [], '-', color='0')
ball_6, = plt.plot([], [], 'o', color='r')

ani = FuncAnimation(fig, animate, frames=frames, interval=30)
ani.save("gifs/task2.gif")