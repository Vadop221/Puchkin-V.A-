n = int(input("Введите число: "))
c = []
for i in range(1,n+1):
    z = i ** 2
    if z <= n:
        c.append(z)
for h in c:
    print(h)


n = int(input("Введите число: "))
i = 1
while i ** 2 <= n:
    print(i**2)
    i += 1
    
