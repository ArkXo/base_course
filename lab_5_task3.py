import time

M = int(input("Введите значение M: "))
N = int(input("Введите значение N: "))

timer = time.time()
for i in range(M+1):
    print("M =", i)
    time.sleep(1)
    for j in range(N+1):
        print("N = ", j)
        time.sleep(1)

print(f'Время работы - {time.time() - timer} секунд')