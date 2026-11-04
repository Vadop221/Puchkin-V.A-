def gef(x, y, a, b, R):
    if (x - a)**2 + (y - b)**2 < R**2:
        return True
    else:
        return False


a = float(input("Введите координату a: "))
b = float(input("Введите координату b: "))
R = float(input("Введите радиус: "))

p1 = float(input("Введите x точки P: "))
p2 = float(input("Введите y точки P: "))

f1 = float(input("Введите x точки F: "))
f2 = float(input("Введите y точки F: "))

l1 = float(input("Введите x точки L: "))
l2 = float(input("Введите y точки L: "))

count = 0

if gef(p1, p2, a, b, R):
    count += 1

if gef(f1, f2, a, b, R):
    count += 1

if gef(l1, l2, a, b, R):
    count += 1

print("Количество точек внутри окружности:", count)
