x = 3
y = 4

z = complex(x, y)
print(z)

w = complex(y, x)
print(z+w)

s = "hello"
print(s[0])

# s[0] = "H"
# print(s)

t = (1, 4, 9)
print(t)
print(t[0])

t = ([1, 2], [3])
t[0][0] = 0
print(t)

t[0].append(3)
print(t)

d = {"al":4, 4:"al", "str":"Hello"}
print(d["str"])
d["str"] = "Good"
print(d)