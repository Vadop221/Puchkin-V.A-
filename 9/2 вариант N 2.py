n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))

A = []

for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)

print("Исходная матрица:")
for row in A:
    print(row)

for i in range(n):
    A[i][0], A[i][-1] = A[i][-1], A[i][0]

print("Полученная матрица:")
for row in A:
    print(row)
