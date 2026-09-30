import math

x= 0.1722
y= 6.33
z= 3.25 * (10**-4)

a = 5 *  math.atan(x)
b= 1/4 * math.acos(x)
c= x+3 * abs(x-y) + x**2
d= abs(x-y) * z+(x**2)

s= a-b * c/d

print(f"s={s:.3f}")
