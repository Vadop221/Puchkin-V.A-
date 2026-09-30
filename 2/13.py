import math

x=17.421
y=10.365*(10**-3)
z=0.828*(10**5)

a= ((x-1)**(1/3))
b= (y + a)**(1/4)
c= abs(x-y)
d= ((math.sin(z)**2)+math.tan(z))

s= b / (c*d)

print(f"s={s:.6f}")
