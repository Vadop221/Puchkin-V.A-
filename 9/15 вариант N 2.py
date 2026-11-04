n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))

A = []

for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)

max_sum = None
max_row = -1

for i in range(n):
    odd = True
    total = 0

    for j in range(m):
        if A[i][j] % 2 == 0:
            odd = False
            break
        total += abs(A[i][j])

    if odd:
        if max_sum is None or total > max_sum:
            max_sum = total
            max_row = i

if max_row == -1:
    print("Строк, состоящих только из нечётных элементов, нет.")
else:
    print("Номер строки:", max_row + 1)
    print("Строка:", A[max_row])
    print("Максимальная сумма модулей:", max_sum)
