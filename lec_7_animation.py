import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots() # Создание пространства и подпространства

anim_object, = plt.plot([], [], '-', lw=2) # Объект анимации

xdata, ydata = [], [] # Координаты объекта анимации

ax.set_xlim(0, 2*np.pi) # Пределы изменения переменной Х
ax.set_ylim(-1, 1) # Пределы изменения переменной У

# Функция подстановки координат в объект анимации
def update(frame):
    xdata.append(frame) # Рассщет координаты Х
    ydata.append(np.sin(frame)) # Рассщет координаты У
    anim_object.set_data(xdata, ydata) # Передача координат
    return anim_object,

ani = FuncAnimation(fig, # Стандартный вызов пространства
                    update, # Вызов функции подстановки координат
                    frames=np.arange(0, 2*np.pi, 0.1),
                    interval=100 # Интервал между кадрами,
                    )            # по умолчанию 200 милисекунд

ani.save('animation_1.gif')