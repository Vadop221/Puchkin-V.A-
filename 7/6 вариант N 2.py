a = []

for i in range(10):
    x = int(input())
    a.append(x)

s = 0

for z in range(10):
    if a[z] > 5:
        s = s + a[z]

print("Сумма:", s)
