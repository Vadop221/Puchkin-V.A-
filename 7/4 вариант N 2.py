n = int(input("Введите количество элементов: "))

a = []

for i in range(n):
    x = int(input())
    a.append(x)

b = []

for z in range(n):
    if a[z] % 2 != 0:
        b.append(a[z])

if len(b) == 0:
    print("Нечётных чисел нет")
else:
    b.sort(reverse=True)
    print(b)
