import math

x = 16.55*(10**-3)
y = -2.75
z = 0.15

a = math.sqrt(10 * (x ** (1 / 3) + x ** (y + 2)))
b = math.asin(z) ** 2 - abs(x - y)

s = a * b

print(f"s = {s:.4f}")
