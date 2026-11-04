import math

a = float(input("Введите первую сторону: "))
b = float(input("Введите вторую сторону: "))
c = float(input("Введите третью сторону: "))
d = float(input("Введите четвёртую сторону: "))
e = float(input("Введите диагональ: "))

p1 = (a + b + e) / 2
p2 = (c + d + e) / 2

s1 = math.sqrt(p1 * (p1 - a) * (p1 - b) * (p1 - e))
s2 = math.sqrt(p2 * (p2 - c) * (p2 - d) * (p2 - e))

S = s1 + s2

print("Площадь четырёхугольника:", S)
