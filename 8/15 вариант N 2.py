import math

def distance(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x2 - x1)**2 +
                     (y2 - y1)**2 +
                     (z2 - z1)**2)


points = []

names = ["X", "Y", "Z", "T"]

for i in range(4):
    x = float(input("Введите координату x: "))
    y = float(input("Введите координату y: "))
    z = float(input("Введите координату z: "))

    points.append((x, y, z))

dmin = float('inf')
name1 = ""
name2 = ""

for i in range(4):
    for j in range(i + 1, 4):
        d = distance(points[i][0], points[i][1], points[i][2],
                     points[j][0], points[j][1], points[j][2])

        if d < dmin:
            dmin = d
            name1 = names[i]
            name2 = names[j]

print("Минимальное расстояние между точками", name1, "и", name2)
print("Расстояние:", dmin)
