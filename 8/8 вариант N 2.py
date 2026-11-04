def gef(a):
    c = a[0]
    a[0] = a[-1]
    a[-1] = c


m = int(input("Введите длину массива: "))

a = []

for i in range(m):
    x = int(input())
    a.append(x)

print("Исходный массив:", a)

gef(a)

print("Полученный массив:", a)
