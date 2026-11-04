import math

def angle(x, y):
    return math.atan2(abs(y), x)


x1 = float(input("Введите x точки X: "))
x2 = float(input("Введите y точки X: "))

y1 = float(input("Введите x точки Y: "))
y2 = float(input("Введите y точки Y: "))

z1 = float(input("Введите x точки Z: "))
z2 = float(input("Введите y точки Z: "))

ax = angle(x1, x2)
ay = angle(y1, y2)
az = angle(z1, z2)

if ax <= ay and ax <= az:
    print("Искомая точка X:", x1, x2)
elif ay <= ax and ay <= az:
    print("Искомая точка Y:", y1, y2)
else:
    print("Искомая точка Z:", z1, z2)
