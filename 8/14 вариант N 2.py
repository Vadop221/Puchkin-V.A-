import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


points = []

names = ["X", "Y", "Z", "P"]

for i in range(4):
    x = float(input("Введите координату x: "))
    y = float(input("Введите координату y: "))
    points.append((x, y))

dmax = 0
name1 = ""
name2 = ""

for i in range(4):
    for j in range(i + 1, 4):
        d = distance(points[i][0], points[i][1],
                     points[j][0], points[j][1])

        if d > dmax:
            dmax = d
            name1 = names[i]
            name2 = names[j]

print("Наибольшее расстояние между точками", name1, "и", name2)
print("Расстояние:", dmax)
