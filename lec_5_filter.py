names = ["sasa", "df", "dsds"]
ages = [12,43,65]

def func(user):
    name, age = user
    return age > 21

users = list(zip(names, ages))
fil = list(filter(func, users))
print(fil)