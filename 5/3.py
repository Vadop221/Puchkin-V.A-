n = int(input("Введите число: "))

step = 0
res = 1
while res * 2 <= n:
    res *= 2
    step += 1
print(step,res)
