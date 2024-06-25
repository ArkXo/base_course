import numpy as np

mas = []
while len(mas) <= 10:
    a = input()
    if a == " ":
        break
    else:
        mas.append(int(a))

print(mas)