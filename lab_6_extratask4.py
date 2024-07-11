import matplotlib.pyplot as plt
import numpy as np

# def steps(n):
#     x = np.arrange(0, n+1, 1)
#     y = np.array([1])
#     for i in range(0, n+1):

x = np.arange(0, 3, 1)
for i in range(0, 3):
    new_x = np.insert(x, i, x[i])
print(new_x)