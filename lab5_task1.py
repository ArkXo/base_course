def prime_gen(n):
    prime_num = []
    for num in range(2, n + 1):
        if  num % prime_num[i for i in range(len(prime_num))] == 0:
            break
        else:
            prime_num.append(num)
            yield num**2

gen = prime_gen(8)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))