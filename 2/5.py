import math

x = -15.246
y = 4.642 * (10**-2)
z = 21

a = y ** (-math.sqrt(abs(x)))
b = x - y / 2
c = math.log(a)
d = math.sin(math.atan(z)) ** 2

s = c * b + d

print(f"s = {s:.3f}")
