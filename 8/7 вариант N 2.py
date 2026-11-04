n = int(input("Введите число: "))

a = oct(n)[2:]

a = a.zfill(10)

print(a)
