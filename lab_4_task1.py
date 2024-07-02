import numpy as np

def average(array):
    av = 0
    for i in range(0, len(array)):
        av += array[i]
    av = av / len(array)
    return av

array = np.array([])
while 1:
    a = input()
    if a == "":
        break
    a = int(a)
    array = np.append(array, [a])

print(average(array))

print(np.mean(array))