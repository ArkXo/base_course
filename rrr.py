from tkinter import *
import matplotlib.pyplot as plt
import scipy.interpolate as sc
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Для встраивания графика в Tkinter

x = []
y = []

class Paint(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.color = "black"
        self.brush_size = 1
        self.width = 900
        self.height = 600
        self.setUI()

    def draw(self, event):
        self.canv.create_oval(event.x - 2, event.y - 2, event.x + 2, event.y + 2,
                              fill=self.color, outline=self.color)
        
        x.append(event.x)
        y.append(-event.y)

    def setUI(self):
        self.pack(fill=BOTH, expand=1)
        self.canv = Canvas(self, bg="white", width=self.width, height=self.height)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.canv.grid(padx=1, pady=1, sticky=W+E+N+S)
        self.canv.bind("<B1-Motion>", self.draw)
        
        # Рисуем сетку
        self.draw_grid()

    def draw_grid(self):
        """Рисует координатную сетку на Canvas с разметкой."""
        step = 50  # Шаг сетки
        width = self.width
        height = self.height

        # Вертикальные линии с разметкой
        for i in range(0, width+step, step):
            self.canv.create_line(i, 0, i, height+step, fill="gray", dash=(1, 5))
            if i != width // 2:  # Не рисуем метку для центральной оси Y
                self.canv.create_text(i, height - 10, text=str(i - width // 2), fill="black", font=("Arial", 8))

        # Горизонтальные линии с разметкой
        for i in range(0, height+step, step):
            self.canv.create_line(0, i, width+step, i, fill="gray", dash=(1, 5))
            if i != height - step:  # Не рисуем метку для нижней грани
                self.canv.create_text(10, i, text=str(height // 2 - i), fill="black", font=("Arial", 8), anchor=W)

        # Ось X (горизонтальная линия внизу)
        self.canv.create_line(0, height//2, width+step, height//2, fill="black", width=2)

        # Ось Y (вертикальная линия по центру)
        self.canv.create_line(width // 2, 0, width // 2, height, fill="black", width=2)


def calculate_center_of_mass(x, y):
    """
    Вычисляет центр масс многоугольника по координатам его вершин.
    :param x: Список x-координат вершин.
    :param y: Список y-координат вершин.
    :return: Координаты центра масс (Cx, Cy).
    """
    n = len(x)
    A = 0.0
    Cx = 0.0
    Cy = 0.0

    for i in range(n):
        # Циклический индекс
        j = (i + 1) % n
        # Вычисление детерминанта (удвоенная площадь треугольника)
        factor = x[i] * y[j] - x[j] * y[i]
        A += factor
        Cx += (x[i] + x[j]) * factor
        Cy += (y[i] + y[j]) * factor

    A *= 0.5
    Cx /= (6.0 * A)
    Cy /= (6.0 * A)

    return Cx, Cy


def btn_func():
    # Проверка на наличие данных
    if len(x) < 3 or len(y) < 3:
        print("Нарисуйте замкнутую фигуру!")
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
    step = 1000
    mytck, myu = sc.splprep([x_arr, y_arr], s=0)
    xnew, ynew = sc.splev(np.linspace(0, 1, step), mytck)
    ax.plot(xnew, ynew, 'red', label="Approximation")

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

    # Настройка легенды и заголовка
    ax.set_title("Graph with Normals")

    # Вычисляем центр масс
    Cx, Cy = calculate_center_of_mass(x, y)
    ax.scatter(Cx, Cy, color='blue', label="Center of Mass", zorder=5)
    

    # Встраиваем график в Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame1)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=BOTH, expand=True)

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

frame1 = Frame(master=frame0, width=w, height=h)
frame1.pack(fill=BOTH, expand=True)

frame2 = Frame(master=root, width=2, bg="black")
frame2.pack(fill=Y, side=LEFT)

frame3 = Frame(master=root, width=200, bg="gray")
frame3.pack(fill=BOTH, side=LEFT, expand=True)

button = Button(master=frame3, text="Сохранить!", command=btn_func)
button.place(x=98, y=500)

app = Paint(frame1)  # Передаем размеры окна
root.mainloop()

