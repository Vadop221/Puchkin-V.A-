a = []

for i in range(8):
    x = int(input())
    a.append(x)

for z in range(8):
    if a[z] < 15:
        a[z] = a[z] * 2
print(a)
