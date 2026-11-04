n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))

A = []

for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)

min_product = None
min_column = -1

for j in range(m):
    product = 1
    suitable = True

    for i in range(n):
        if abs(A[i][j]) > 10:
            suitable = False
            break
        product *= A[i][j]

    if suitable:
        if min_product is None or product < min_product:
            min_product = product
            min_column = j

if min_column == -1:
    print("Подходящих столбцов нет.")
else:
    if min_column < m - 1:
        neighbor = min_column + 1
    else:
        neighbor = min_column - 1

    for i in range(n):
        A[i][min_column], A[i][neighbor] = A[i][neighbor], A[i][min_column]

    print("Полученная матрица:")
    for row in A:
        print(row)

    print("Минимальное произведение:", min_product)
