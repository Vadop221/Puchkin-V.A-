n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))

A = []

for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)

print("Исходная матрица:")
for row in A:
    print(row)

max_element = A[0][0]
min_element = A[0][0]

max_i = 0
max_j = 0
min_i = 0
min_j = 0

for i in range(n):
    for j in range(m):
        if A[i][j] > max_element:
            max_element = A[i][j]
            max_i = i
            max_j = j

        if A[i][j] < min_element:
            min_element = A[i][j]
            min_i = i
            min_j = j

A[max_i][max_j], A[min_i][min_j] = A[min_i][min_j], A[max_i][max_j]

print("Полученная матрица:")
for row in A:
    print(row)
