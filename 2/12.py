import math

x=3.251
y= 0.325
z=0.466*(10**-4)

a=(2**(y**x))
b=((3**x)**y)
c=y*(math.atan(z)-(1/3))
d=abs(x)
e=1/((y**2)+1)

s= a+b - c/(d+e)
print(f"s={s:.5f}")
