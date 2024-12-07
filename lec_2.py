	
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
 
# Определяем переменную величину
frames = 500
seconds_in_year = 365 * 24 * 60 * 60
years = 1
t = np.linspace(0, years*seconds_in_year, frames)
 
# Определяем функцию для системы диф. уравнений
def move_func(s, t):
    (x1, v_x1, y1, v_y1,
     x2, v_x2, y2, v_y2) = s
 
    dxdt1 = v_x1
    dv_xdt1 = - G * M * x1 / (x1**2 + y1**2)**1.5
    dydt1 = v_y1
    dv_ydt1 = - G * M * y1 / (x1**2 + y1**2)**1.5
 
    dxdt2 = v_x2
    dv_xdt2 = - G * M * x2 / (x2**2 + y2**2)**1.5
    dydt2 = v_y2
    dv_ydt2 = - G * M * y2 / (x2**2 + y2**2)**1.5
 
    return (dxdt1, dv_xdt1, dydt1, dv_ydt1,
            dxdt2, dv_xdt2, dydt2, dv_ydt2)

G = 6.67 * 10**(-11)
M = 1.98 * 10**(30)
 
x10 = 149 * 10**9
v_x10 = 0
y10 = 0
v_y10 = 30000
 
x20 = 0
v_x20 = -47360
y20 = 0.387 * 149 * 10**9
v_y20 = 0
 
s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20)

sol = odeint(move_func, s0, t)

x1 = sol[:, 0]
y1 = sol[:, 2]

x2 = sol[:, 4]
y2 = sol[:, 6]

def animate(i):
    earth.set_data([x1[i]], [y1[i]])
    earth_line.set_data([x1[:i]], [y1[:i]])
    
    mercury.set_data([x2[i]], [y2[i]])
    mercury_line.set_data([x2[:i]], [y2[:i]])

fig, ax = plt.subplots()

earth, = plt.plot([], [], 'o', color='b')
earth_line, = plt.plot([], [], '-', color='b')

mercury, = plt.plot([], [], 'o', color='r')
mercury_line, = plt.plot([], [], '-', color='r')

plt.plot([0], [0], 'o', color='y', ms=20)

plt.axis("equal")
edge = 2 * x10
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani = FuncAnimation(fig, animate, frames=frames, interval=30)
ani.save("earth_merc.gif")