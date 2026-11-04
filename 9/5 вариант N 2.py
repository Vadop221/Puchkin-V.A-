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
    min_index = A[i].index(min(A[i]))

    if A[i][min_index] % 2 == 0:
        A[i][min_index] = 0
    else:
        A[i][min_index] = 1

print("Полученная матрица:")
for row in A:
    print(row)
