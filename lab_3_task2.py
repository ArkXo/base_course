import lab_3_task1 as cons
import numpy as np

h = 100
a = cons.pi / 3
b = cons.pi / 6
v = np.sqrt((cons.g * h * np.tan(b)**2)/(2 * np.cos(a)**2 * (1 - np.tan(b) * np.tan(a))))
print(v)

