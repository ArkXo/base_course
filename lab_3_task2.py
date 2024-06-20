import lab_3_task1 as const
import numpy as np

h = 100
a = const.pi / 3
b = const.pi / 6
v = np.sqrt((const.g * h * np.tan(b)**2)/(2 * np.cos(a)**2 * (1 - np.tan(b) * np.tan(a))))
print(v)

T = 200
E = 300
N = (2 * const.ht * (const.e**( (-E) / (const.k * T))) * (E ** ( T/2 ))) / (np.sqrt(const.pi) * (const.k * T)**(3/2))
print(N)