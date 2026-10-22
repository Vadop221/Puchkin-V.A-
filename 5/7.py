con = 0
n = int(input("Введите число: "))
z = n

while n != 0:
    n = int(input("Введите число: "))
    if n != 0 and n > z:
        con += 1
    z = n

print(con)
