import math

x=2.444
y=0.869*(10**-2)
z=-0.13*(10**3)

a=(x**(y+1))
b=math.exp(y-1)
c=a+b
d=(1+x*abs(y-math.tan(z)))
e=c/d
f=(1+abs(y-x))
g=(abs(y-x)**2)/2
h=(abs(y-x)**3)/3

s=e*f+g-h


print(f"s={s:.6f}")
