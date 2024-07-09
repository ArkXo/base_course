def fib(n):
    fib_1 = 0
    fib_2 = 1
    if n > 2:
        for i in range(n-2):
            fib_n = fib_1 + fib_2
            fib_1, fib_2 = fib_2, fib_n
    elif n == 1:
        fib_n = fib_1
    elif n == 2:
        fib_n = fib_2
    return fib_n

print(fib(int(input("Введите значение n: "))))