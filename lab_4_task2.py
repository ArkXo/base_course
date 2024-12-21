import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
 
# Определяем переменную величину
frames = 500
seconds_in_year = 365 * 20
years = 1 
t = np.linspace(0, years*seconds_in_year, frames)

k = 9 * 10**9
Q = 150
ae = 10**6
v = 900
 
s0_1 = ae, 0, 0, -v, 3, 5
s0_2 = 0.723*ae, 1.5*v, 0.2*ae, -v/np.sqrt(0.723), 4, 2
s0_3 = -0.8*ae, -1.5*v, 1.7*ae, -1.2*v, 6, 2
s0_4 = 1.52*ae, -0.12*v, -0.3*ae, -v/np.sqrt(1.52), -5, 3
s0_5 = -2*ae, 0.14*v, -1.8*ae, -v/np.sqrt(2), -3, 1
s0_6 = 1.57*ae, -2.3*v, 1.3*ae, -v/np.sqrt(2.57), -6, 2

def move_func(s, t):
    x, v_x, y, v_y,q, m = s
    dx_dt = v_x
    dvx_dt = -(k * Q * abs(q) / m) * x / (x**2 + y**2)**1.5
    dy_dt = v_y
    dvy_dt = -(k * Q * abs(q) / m) * y / (x**2 + y**2)**1.5

    return dx_dt, dvx_dt, dy_dt, dvy_dt, 0, 0

sol_1 = odeint(move_func, s0_1, t)
sol_2 = odeint(move_func, s0_2, t)
sol_3 = odeint(move_func, s0_3, t)
sol_4 = odeint(move_func, s0_4, t)
sol_5 = odeint(move_func, s0_5, t)
sol_6 = odeint(move_func, s0_6, t)

x_1 = sol_1[:, 0]
y_1 = sol_1[:, 2]

x_2 = sol_2[:, 0]
y_2 = sol_2[:, 2]

x_3 = sol_3[:, 0]
y_3 = sol_3[:, 2]

x_4 = sol_4[:, 0]
y_4 = sol_4[:, 2]

x_5 = sol_5[:, 0]
y_5 = sol_5[:, 2]

x_6 = sol_6[:, 0]
y_6 = sol_6[:, 2]

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
edge = 4 * ae
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

plt.plot([0], [0], 'o', color='y', ms=10)

ball_1_line, = plt.plot([], [], color='m', linestyle='dashed')
ball_1, = plt.plot([], [], 'o', color='m')

ball_2_line, = plt.plot([], [], color='g', linestyle='dashed')
ball_2, = plt.plot([], [], 'o', color='g')

ball_3_line, = plt.plot([], [], color='b', linestyle='dashed')
ball_3, = plt.plot([], [], 'o', color='b')

ball_4_line, = plt.plot([], [], color='r', linestyle='dashed')
ball_4, = plt.plot([], [], 'o', color='r')

ball_5_line, = plt.plot([], [], color='tab:gray', linestyle='dashed')
ball_5, = plt.plot([], [], 'o', color='tab:gray')

ball_6_line, = plt.plot([], [], color='tab:orange', linestyle='dashed')
ball_6, = plt.plot([], [], 'o', color='tab:orange')

ani = FuncAnimation(fig, animate, frames=frames, interval=30)
ani.save("task2.gif")