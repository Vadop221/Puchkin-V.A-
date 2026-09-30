import math

x = 6.251
y = 0.827
z = 25.001

a= (abs(x)**(1/3))
b= y**a
c= (math.cos(y)**3)
d= abs(x-y)
e= d * (1 + (math.sin(z)**2)/math.sqrt(x+y))
f= math.exp(abs(x-y))+(x/2)

s = b+c*e/f
print(f"s={s:.5f}")
