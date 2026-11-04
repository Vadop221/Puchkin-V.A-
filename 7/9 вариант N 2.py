a = []
b = []

print("Введите элементы массива A:")

for i in range(10):
    x = int(input())
    a.append(x)

print("Введите элементы массива B:")

for i in range(10):
    x = int(input())
    b.append(x)

print("Исходный массив A:", a)
print("Исходный массив B:", b)

for z in range(10):
    c = a[z]
    a[z] = b[z]
    b[z] = c

print("Преобразованный массив A:", a)
print("Преобразованный массив B:", b)
