n = int(input("Введите размер матрицы: "))

A = []

for i in range(n):
    row = list(map(float, input().split()))
    A.append(row)

diagonal = []

for i in range(n):
    diagonal.append(A[i][i])

trace = sum(diagonal)

print("Диагональные элементы:", diagonal)
print("След матрицы:", trace)

if trace != 0:
    for i in range(n):
        if (i + 1) % 2 == 0:
            for j in range(n):
                A[i][j] = A[i][j] / trace

    print("Полученная матрица:")
    for row in A:
        print(row)
else:
    print("След равен нулю, деление невозможно.")
