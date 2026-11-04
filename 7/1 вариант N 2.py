n = int(input("Введите количество элементов: "))

a = []

for i in range(n):
    x = float(input())
    a.append(x)

sred = sum(a)/n

for i in range(n):
    if a[i] == 0:
        a[i] = sred
        
print("Результат:",a)
