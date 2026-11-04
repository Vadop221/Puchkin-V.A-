m = int(input("Введите количество строк: "))
n = int(input("Введите количество столбцов: "))

D = []

for i in range(m):
    row = list(map(int, input().split()))
    D.append(row)

k = int(input("Введите номер строки k: "))

print("Исходная матрица:")
for row in D:
    print(row)

for i in range(n):
    for j in range(n - 1 - i):
        if D[k - 1][j] > D[k - 1][j + 1]:
            for r in range(m):
                D[r][j], D[r][j + 1] = D[r][j + 1], D[r][j]

print("Полученная матрица:")
for row in D:
    print(row)
