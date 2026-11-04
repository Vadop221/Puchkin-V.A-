a = []

n = int(input("Введите количество элементов: "))

for i in range(n):
    x = int(input())
    a.append(x)

imin = 0
imax = 0

for z in range(n):
    if a[z] < a[imin]:
        imin = z
    if a[z] > a[imax]:
        imax = z

a[imin], a[imax] = a[imax], a[imin]

print(a)
