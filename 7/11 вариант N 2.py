n = int(input("Введите количество элементов: "))

a = []

for i in range(n):
    x = int(input())
    a.append(x)

b = []

for z in range(n):
    if a[z] % 2 == 0 and a[z] < 10:
        b.append(a[z])

if len(b) == 0:
    print("Таких чисел нет")
else:
    b.sort()
    print(b)
