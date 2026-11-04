n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))

A = []

for i in range(n):
    row = list(map(float, input().split()))
    A.append(row)

print("Исходная матрица:")
for row in A:
    print(row)

for i in range(n - 1):
    for j in range(m):
        A[i][j] = A[i][j] - A[n - 1][j]

print("Полученная матрица:")
for row in A:
    print(row)
