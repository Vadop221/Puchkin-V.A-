con = 0
n = int(input("Введите число: "))
summa = 0
while n != 0:
    con += 1
    summa += n
    n = int(input("Введите число: "))
    if n == 0:
        summa /= con

print(con)
print(summa)
