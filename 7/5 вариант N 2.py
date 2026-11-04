a = []

for i in range(10):
    x = int(input())
    a.append(x)

b = []

for z in range(10):
    if a[z] not in b:
        b.append(a[z])

print(b)
