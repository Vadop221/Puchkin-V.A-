n = int(input("Введите количество элементов: "))

a = []

for i in range(n):
    x = int(input())
    a.append(x)

b = []

c = []

for z in range(n):
    if a[z] > 0:
        b.append(a[z])
    else:
        c.append(a[z])

print(a,b,c)
