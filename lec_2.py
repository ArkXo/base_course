a = range(3)

print(id(a))
print(type(a))

new_a = iter(a)
print(id(new_a))
print(type(new_a))

print(next(new_a))
print(next(new_a))
print(next(new_a))