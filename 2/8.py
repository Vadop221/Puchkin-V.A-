import math

x=-2.235*(10**-2)
y=2.23
z=15.221

a= abs(x-y)
b= math.exp(a) * (a**(x+y))
c= math.atan(x)+math.atan(z)
d= (x**6 + math.log(y)**2)**(1/3)

s= b/c + d
print(f"s = {s:.4f}")
