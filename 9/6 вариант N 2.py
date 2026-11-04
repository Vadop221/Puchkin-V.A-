n = int(input("Введите размер матрицы (нечетное число): "))

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
    if A[i][i] > max_element:
        max_element = A[i][i]
        max_i = i
        max_j = i

    if A[i][n - 1 - i] > max_element:
        max_element = A[i][n - 1 - i]
        max_i = i
        max_j = n - 1 - i

center = n // 2

A[max_i][max_j], A[center][center] = A[center][center], A[max_i][max_j]

print("Полученная матрица:")
for row in A:
    print(row)
