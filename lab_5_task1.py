import numpy as np
import random as rnd

N = int(input("Введите значание длины массивов: "))

array_1 = np.array(N)
array_2 = np.array(N)
array_3 = np.array(N)

for i in range(N):
    array_1 = np.append(array_1, [rnd.randint(0, 100)])
    array_2 = np.append(array_2, [rnd.randint(0, 100)])
    array_3 = np.append(array_3, [rnd.randint(0, 100)])

if max(array_1) >= max(array_2) and max(array_3):
    maximum = max(array_1)
elif max(array_2) >= max(array_1) and max(array_3):
    maximum = max(array_2)
else:
    maximum = max(array_3)
print("Наибольший элемент: ", maximum)
print("Сумма всех элементов: ", sum(array_1)+sum(array_2)+sum(array_3))