import numpy as np

g = 9.8

def energy(m, h, v):
    E = (m * v**2)/2 + m * g * h
    return E

print(energy(int(input("Задайте значение массы: ")), int(input("Задайте значение высоты: ")), int(input("Задайте значение скорости: "))))