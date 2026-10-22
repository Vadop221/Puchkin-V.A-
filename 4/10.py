n = int(input("Введите N: "))
k = int(input("Введите K: "))

a = 0
b = 1
s = 0

for i in range(k + n - 1):
    if i >= k - 1:
        s += a
    a, b = b, a + b

print(s)
