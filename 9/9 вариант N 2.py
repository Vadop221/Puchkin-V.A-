n = int(input("Введите размер матрицы: "))

A = []

for i in range(n):
    row = list(map(float, input().split()))
    A.append(row)

print("Исходная матрица:")
for row in A:
    print(row)

max_element = abs(A[0][0])
max_i = 0
max_j = 0

for i in range(n):
    for j in range(n):
        if abs(A[i][j]) > max_element:
            max_element = abs(A[i][j])
            max_i = i
            max_j = j

B = []

for i in range(n):
    if i != max_i:
        row = []

        for j in range(n):
            if j != max_j:
                row.append(A[i][j])

        B.append(row)

print("Максимальный по модулю элемент:", A[max_i][max_j])

print("Полученная матрица:")
for row in B:
    print(row)
