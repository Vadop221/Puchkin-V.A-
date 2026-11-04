n = int(input("Введите размер матрицы: "))

A = []

for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)

for i in range(n):
    for j in range(n):
        if A[i][j] < 0:
            A[i][j] = 0
        elif A[i][j] > 0:
            A[i][j] = 1

print("Нижняя треугольная матрица:")

for i in range(n):
    for j in range(n):
        if i >= j:
            print(A[i][j], end=" ")
        else:
            print(" ", end=" ")
    print()
