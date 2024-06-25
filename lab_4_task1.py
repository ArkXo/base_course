import numpy as np

def average(array):
    av = 0
    for i in range(0, len(array)):
        av += array[i]
    av = av / 2
    return av
a = np.array(list())
# print(average(np.array([list(input()), int])))