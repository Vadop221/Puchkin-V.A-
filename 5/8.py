n = int(input("Введите число: "))
prev = n

con = 1
max_con = 1

while n != 0:
    n = int(input("Введите число: "))

    if n == prev and n != 0:
        con += 1
    elif n != 0:
        con = 1

    if con > max_con:
        max_con = con

    prev = n

print(max_con)
