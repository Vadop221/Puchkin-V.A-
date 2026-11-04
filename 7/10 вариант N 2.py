a = []

for i in range(15):
    x = int(input())
    a.append(x)

print("Первоначальный массив:", a)

for z in range(15):
    if a[z] < 10:
        a[z] = 0
    elif a[z] > 20:
        a[z] = 1

print("Преобразованный массив:", a)
