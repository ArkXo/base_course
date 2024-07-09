def deg(a, n):
    an = 1
    for i in range(n):
        an *= a
    print(f"{a} ** {n} =", end=" ")
    return an

print(deg(int(input("Введите значение a: ")), int(input("Введите значение n: "))))