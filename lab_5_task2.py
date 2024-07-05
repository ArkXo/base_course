import numpy as np

name = "ArteymKoloskov"
name = "_".join(name)

name = name.upper()
array_1 = np.array([])
for i in name:
    array_1 = np.append(array_1, [ord(i)])

name = name.lower()
array_2 = np.array([])
for i in name:
    array_2 = np.append(array_2, [ord(i)])

print(f" Наибольшее значение первого массива: {max(array_1)}, минимальное значение: {min(array_1)}")
print(f" Наибольшее значение первого массива: {max(array_2)}, минимальное значение: {min(array_2)}")
