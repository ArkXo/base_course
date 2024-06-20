import numpy as np
from lab_3_task1 import g

v0x = int(input("Введите скорость тела: "))
x0 = int(input("Введите начальные координаты по x: "))
y0 = int(input("Введите начальные координаты по y: "))

a = ["t", "x", 'y']
mas = np.array([a])
print(mas)
for t in range(0, 6):
    x = x0 + v0x * t
    y = y0 + v0x * t - g * t**2 / 2

