import numpy as np

def func(x):
    y = x**2
    return y

print("Введите значение параметров:")
a = int(input("Введите значение a: "))
b = int(input("Введите значение b: "))
N = int(input("Введите значение N: "))

array = np.linspace(a, b, N+2)
array = np.delete(array, [0, -1])
print(func(array))
