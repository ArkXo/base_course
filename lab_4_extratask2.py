def fib(n):
    fib_1 = 0
    fib_2 = 1
    for i in range(n-1):
        fib_n = fib_1 + fib_2
        fib_1, fib_2 = fib_2, fib_n
    return fib_n

print(fib(int(input("Введите значение n: "))))