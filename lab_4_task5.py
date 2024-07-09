import numpy as np

def area(figure):
    if figure == "круг":
        r = int(input("Введите значение радиуса: "))
        area = np.pi* (r**2)
    if figure == "прямоугольник":
        a = int(input("Введите значение длины: "))
        b = int(input("Введите значение ширины: "))
        area = a*b
    if figure == 'треугольник':
        a = int(input("Введите значение основания: "))
        h = int(input("Введите значение высоты: "))
        area = (a*h)/2
    return area

print(area(input("Ваедите название фигуры: ")))