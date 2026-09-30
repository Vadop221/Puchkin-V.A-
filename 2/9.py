import math

x = 1.825 * (10**2)
y = 18.225
z = -3.298 * (10**-2)

a = abs(x**(y/x) - (y/x)**(1/3))

b = (y-x) * (math.cos(y) - z/(y-x)) / (1+(y-x)**2)

s = a + b

print(f"s = {s:.5f}")
