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
M = 1.989 * 10**(30)
ae = 149.6 * 10**9
v_earth = 29800
 
s0_merc = 0.387*ae, 0, 0, v_earth/np.sqrt(0.387)
s0_ven = 0.723*ae, 0, 0, v_earth/np.sqrt(0.723)
s0_earth = 1*ae, 0, 0, v_earth
s0_mars = 1.52*ae, 0, 0, v_earth/np.sqrt(1.52)
s0_pha = 2.4*ae, 0, 0, ( (G*M * (1-0.88994)) / (2.4*ae) )**(1/2)

def move_func(s, t):
    x, v_x, y, v_y = s
    dx_dt = v_x
    dvx_dt = - G * M * x / (x**2 + y**2)**1.5
    dy_dt = v_y
    dvy_dt = - G * M * y / (x**2 + y**2)**1.5

    return dx_dt, dvx_dt, dy_dt, dvy_dt

sol_merc = odeint(move_func, s0_merc, t)
sol_ven = odeint(move_func, s0_ven, t)
sol_earth = odeint(move_func, s0_earth, t)
sol_mars = odeint(move_func, s0_mars, t)
sol_pha = odeint(move_func, s0_pha, t)

x_merc = sol_merc[:, 0] / ae
y_merc = sol_merc[:, 2] / ae

x_ven = sol_ven[:, 0] / ae
y_ven = sol_ven[:, 2] / ae

x_earth = sol_earth[:, 0] / ae
y_earth = sol_earth[:, 2] / ae

x_mars = sol_mars[:, 0] / ae
y_mars = sol_mars[:, 2] / ae

x_pha = sol_pha[:, 0] / ae
y_pha = sol_pha[:, 2] / ae


def animate(i):
    ball_merc.set_data([x_merc[i]], [y_merc[i]])
    ball_merc_line.set_data([x_merc[:i]], [y_merc[:i]])

    ball_ven.set_data([x_ven[i]], [y_ven[i]])
    ball_ven_line.set_data([x_ven[:i]], [y_ven[:i]])

    ball_earth.set_data([x_earth[i]], [y_earth[i]])
    ball_earth_line.set_data([x_earth[:i]], [y_earth[:i]])    
    
    ball_mars.set_data([x_mars[i]], [y_mars[i]])
    ball_mars_line.set_data([x_mars[:i]], [y_mars[:i]])

    ball_pha.set_data([x_pha[i]], [y_pha[i]])
    ball_pha_line.set_data([x_pha[:i]], [y_pha[:i]])

fig, ax = plt.subplots()
plt.axis("equal")
edge = 2.5
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

plt.plot([0], [0], 'o', color='y', ms=20)

ball_merc_line, = plt.plot([], [], '-', color='0')
ball_merc, = plt.plot([], [], 'o', color='m')

ball_ven_line, = plt.plot([], [], '-', color='0')
ball_ven, = plt.plot([], [], 'o', color='g')

ball_earth_line, = plt.plot([], [], '-', color='0')
ball_earth, = plt.plot([], [], 'o', color='b')

ball_mars_line, = plt.plot([], [], '-', color='0')
ball_mars, = plt.plot([], [], 'o', color='r')

ball_pha_line, = plt.plot([], [], '-', color='0')
ball_pha, = plt.plot([], [], 'o', color='tab:gray')

ani = FuncAnimation(fig, animate, frames=frames, interval=30)
ani.save("gifs/task1.gif")