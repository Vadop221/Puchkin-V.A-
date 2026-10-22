n=int(input("Введите кол во чисел: "))

summa = 0

for i in range(n+1):
    summa += i**3
    
print(summa)
