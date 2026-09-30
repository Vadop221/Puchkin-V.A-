import math
x = 14.26
y = -1.22
z = 3.5*(10**-2)

a = 2*math.cos(x-2/3)
b = 1/2 + math.sin(y)**2
c = 1 + (z**2)/(3 - (z**2)/5)
s = (a/b)*c

print("s={0:.6f}".format(s))
