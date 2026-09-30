import math

x = 3.981*(10**-2)
y = -1.625*(10**3)
z = 0.512

a= (2**-x)
b=math.sqrt(x+(abs(y)**(1/4)))
c=math.exp(x-1/math.sin(z))**(1/3)
s = a * b * c
print(f"s={s:.5f}")
