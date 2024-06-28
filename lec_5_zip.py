names = ["sasa", "dsds", "dsds"]
ages = [12,43,65]
isTeenager = [True, False, False]

users = list(zip(names, ages, isTeenager))
print(users)

print("User age: ", dict(zip(names, ages)))