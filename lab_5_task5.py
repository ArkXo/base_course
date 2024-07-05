name = "KoloskovArteymEvgenievich"

up = name.upper()
low = name.lower()

up_new = []
for i in up:
    up_new.append(ord(i))

low_new = []
for i in low:
    low_new.append(ord(i))

print(sum(up_new))
print(sum(low_new))