a = []

for i in range(10):
    x = int(input())
    a.append(x)

sred = sum(a) / 10

for z in range(10):
    if a[z] > sred:
        a[z] = 1

print("Среднее арифметическое:", sred)
print("Преобразованный массив:", a)
