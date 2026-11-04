import math

def median(a, b, c):
    return 0.5 * math.sqrt(2 * b**2 + 2 * c**2 - a**2)


a = float(input("Введите сторону a: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))

ma = median(a, b, c)
mb = median(b, a, c)
mc = median(c, a, b)

print("Медианы исходного треугольника:")
print(ma, mb, mc)

na = median(ma, mb, mc)
nb = median(mb, ma, mc)
nc = median(mc, ma, mb)

print("Медианы нового треугольника:")
print(na, nb, nc)
