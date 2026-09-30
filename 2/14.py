import math

x = 12.3*(10**-1)
y=15.4
z=0.252*(10**3)

a=(y**(x+1))
b=(abs(y-2)**(1/3)+3)
c=a/b
d=x+(y/2)
e=2*abs(x+y)
f=d/e
g=(x+1)**(-1/math.sin(z))

s=c+f*g

print(f"s={s:.4f}")
