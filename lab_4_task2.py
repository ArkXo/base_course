import numpy as np

def multiply(array):
    mul = 1
    for i in range(0, len(array)):
        mul = mul * array[i]
    return mul

array = np.array([])
while 1:
    a = input()
    if a == "":
        break
    a = int(a)
    array = np.append(array, [a])

print(multiply(array))