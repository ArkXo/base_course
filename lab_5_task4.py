import random as rnd

flowers = ["роза", "ландыш", "тульпан"]
colors = ["красный", "жёлтый", "оранжевый", "розовый", "белый"]
colors_rnd = []

for i in range(0, 3):
    colors_rnd.append(rnd.choice(colors))

dicti = dict(zip(flowers, colors_rnd))
print(dicti)