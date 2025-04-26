from tkinter import *
import matplotlib.pyplot as plt
import scipy.interpolate as sc
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Для встраивания графика в Tkinter

from const import *
from class_paint import Paint
from center_mass import calculate_center_of_mass

x = []
y = []

alpha = np.pi/4

def btn_func():
    global temperature_entry

    # Получаем значение температуры из текстового поля
    try:
        global temperature
        temperature = float(temperature_entry.get())
    except ValueError:
        return

    # Проверка на наличие данных
    if len(x) < 3 or len(y) < 3:
        return

    # Закрываем текущее окно рисования
    app.destroy()

    # Создаем фигуру matplotlib
    fig, ax = plt.subplots(figsize=(9, 6))

    # Построение нарисованного объекта
    x.append(x[0])  # Замыкаем фигуру
    y.append(y[0])
    x_arr = np.array(x)
    y_arr = np.array(y)

    ax.plot(x_arr, y_arr, label="Original")

    # Аппроксимация нарисованного объекта
    step = 1500
    mytck, myu = sc.splprep([x_arr, y_arr], s=0)
    xnew, ynew = sc.splev(np.linspace(0, 1, step), mytck)
    ax.plot(xnew, ynew, 'red', label="Approximation")

    global gamma
    gamma = []

    # Разделение на участки с заданной точностью
    acc = 20
    for i in range(0, step, acc):
        try:
            ax.plot([xnew[i], xnew[i+acc]], [ynew[i], ynew[i+acc]], 'green')

            x_h = (xnew[i] + xnew[i+acc]) / 2
            y_h = (ynew[i] + ynew[i+acc]) / 2

            # Нормальный вектор (ненормированный)
            if xnew[0+acc] < xnew[0]:
                x_n = ynew[i+acc] - ynew[i]
                y_n = xnew[i] - xnew[i+acc]
            else:
                x_n = - ynew[i+acc] + ynew[i]
                y_n = - xnew[i] + xnew[i+acc]

            # Единичный нормальный вектор
            norm = np.sqrt(x_n**2 + y_n**2)
            X_n = x_n / norm
            Y_n = y_n / norm

            # Конец нормали (отложено от середины)
            scale = 20  # Длина нормали
            x_end = x_h + scale * X_n
            y_end = y_h + scale * Y_n

            # Рисуем нормаль
            ax.plot([x_h, x_end], [y_h, y_end], 'black')

        except IndexError:
            ax.plot([xnew[i], xnew[0]], [ynew[i], ynew[0]], 'green')

            x_h = (xnew[i] + xnew[0]) / 2
            y_h = (ynew[i] + ynew[0]) / 2

            # Нормальный вектор (ненормированный)
            if xnew[0+acc] < xnew[0]:
                x_n = ynew[0] - ynew[i]
                y_n = xnew[i] - xnew[0]
            else:
                x_n = - ynew[0] + ynew[i]
                y_n = - xnew[i] + xnew[0]

            # Единичный нормальный вектор
            norm = np.sqrt(x_n**2 + y_n**2)
            X_n = x_n / norm
            Y_n = y_n / norm

            # Конец нормали (отложено от середины)
            scale = 20  # Длина нормали
            x_end = x_h + scale * X_n
            y_end = y_h + scale * Y_n

            # Рисуем нормаль
            ax.plot([x_h, x_end], [y_h, y_end], 'black')

        beta = np.arccos((x_end-x_h)/(np.sqrt((x_end-x_h)**2 + (y_end-y_h)**2)))
        if np.arcsin((y_end-y_h)/(np.sqrt((x_end-x_h)**2 + (y_end-y_h)**2)))<0:
            beta = - beta

        if beta >= 0:
            if beta >= alpha:
                if beta - alpha < np.pi/2:
                    gamma.append(beta - alpha)
                    ax.plot([x_h, x_h+50*np.cos(alpha)], [y_h, y_h+50*np.sin(alpha)], 'yellow')
            else:
                if alpha - beta < np.pi/2:
                    gamma.append(alpha - beta)
                    ax.plot([x_h, x_h+50*np.cos(alpha)], [y_h, y_h+50*np.sin(alpha)], 'yellow')
        else:
            if abs(beta) >= np.pi - alpha:
                if 2*np.pi - abs(beta) - alpha < np.pi/2:
                    gamma.append(2*np.pi - abs(beta) - alpha)
                    ax.plot([x_h, x_h+50*np.cos(alpha)], [y_h, y_h+50*np.sin(alpha)], 'yellow')
            else:
                if alpha + abs(beta) < np.pi/2:
                    gamma.append(alpha + abs(beta))
                    ax.plot([x_h, x_h+50*np.cos(alpha)], [y_h, y_h+50*np.sin(alpha)], 'yellow')

    # Настройка легенды и заголовка
    ax.set_title("Graph with Normals")

    # Вычисляем центр масс
    Cx, Cy = calculate_center_of_mass(x, y)
    ax.scatter(Cx, Cy, color='blue', zorder=5)
    

    # Встраиваем график в Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame1)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=BOTH, expand=True)
    energy_calc()
    return temperature


def energy_calc():
    global temperature
    lambda_max = b / temperature

    mu = lambda_max
    sigma = mu / 4

    lambda_array = np.random.normal(mu, sigma, 1000)
    impulse_array = []
    for i in range(0, len(gamma)):
        impulse_array.append(h / lambda_array[i] * np.cos(gamma[i]))
        print(gamma)
    print(impulse_array)

# Размеры окна
w = 900
h = 600

root = Tk()
w_root = 1200
h_root = 600
w_window = root.winfo_screenwidth() // 2 - w_root // 2
h_window = root.winfo_screenheight() // 2 - h_root // 2
root.geometry(f"1200x600+{w_window}+{h_window}")
root.title("Рисуйте")
root.resizable(width=False, height=False)

frame0 = Frame(master=root, width=w, height=h, bg="black")
frame0.pack(fill=BOTH, side=LEFT, expand=True)

frame1 = Frame(master=frame0)
frame1.pack(fill=BOTH, expand=True)

frame2 = Frame(master=root, width=2, bg="black")
frame2.pack(fill=Y, side=LEFT)

frame3 = Frame(master=root, width=200, bg="gray")
frame3.pack(fill=BOTH, side=LEFT, expand=True)

# Метка для текстового поля
temperature_label = Label(master=frame3, text="Температура звезды (K):", bg="gray", fg="white")
temperature_label.place(x=20, y=50)

# Текстовое поле для ввода температуры
temperature_entry = Entry(master=frame3, width=15)
temperature_entry.place(x=20, y=80)

button = Button(master=frame3, text="Сохранить!", command=btn_func)
button.place(x=98, y=500)

app = Paint(frame1, x, y)  # Передаем размеры окна
root.mainloop()
