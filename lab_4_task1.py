import numpy as np

def average(array):
    av = 0
    for i in range(0, len(array)):
        av += array[i]
    av = av / 2
    return av
a = [1, 2, 3]
print(np.array(a))
# print(np.array(list(input())))
print(average(a))
