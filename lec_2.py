	
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