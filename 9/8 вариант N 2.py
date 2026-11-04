n = int(input("Введите размер матрицы: "))

A = []

for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)

print("Исходная матрица:")
for row in A:
    print(row)

B = []

for i in range(n):
    row = []

    for j in range(n):
        row.append(A[j][i])

    B.append(row)

print("Транспонированная матрица:")
for row in B:
    print(row)
