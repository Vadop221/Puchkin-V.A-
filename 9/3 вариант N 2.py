n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))

A = []

for i in range(n):
    row = list(map(float, input().split()))
    A.append(row)

print("Исходная матрица:")
for row in A:
    print(row)

max_element = A[0][0]
max_i = 0
max_j = 0

for i in range(n):
    for j in range(m):
        if A[i][j] > max_element:
            max_element = A[i][j]
            max_i = i
            max_j = j

A[0], A[max_i] = A[max_i], A[0]

for i in range(n):
    A[i][0], A[i][max_j] = A[i][max_j], A[i][0]

print("Полученная матрица:")
for row in A:
    print(row)
