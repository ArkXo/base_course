import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

m_mendal = int(input("Введите сколько мендаля съел человек(кг): ")) # кг
m_tela = int(input("Введите вес человека(кг): "))


k1 = 300 / 100 # мг/г
m_Am = k1 * m_mendal * 1000 # мг

M_Am = 457
M_Hcn = 27
m_Hcn = m_Am * M_Hcn / M_Am

m_smert = 3.4 * m_tela

m0 = m_Hcn
k = 0.01
v = 500 # м/ч
t = np.arange(0, 20, 0.1)

def move_func(s, t):
    m = s

    dm_dt = - k * m

    return dm_dt

s0 = m0
sol = odeint(move_func, s0, t)
print(sol)

fig, ax = plt.subplots()

balls, = plt.plot([], [], 'o', color='b')
balls_lines, = plt.plot([], [], '-', color='b')

def animate(i):
    balls.set_data([t[i]], [sol[i]])
    balls_lines.set_data([t[:i]], [sol[:i]])

ax.set_xlim(0, 20)
ax.set_ylim(0, 272)

ani = FuncAnimation(fig, animate, frames=len(sol), interval=30)
ani.save("HCN.gif")
print(sol[-1])