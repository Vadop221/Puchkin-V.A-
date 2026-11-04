def find_max(a):
    imax = 0
    jmax = 0

    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] > a[imax][jmax]:
                imax = i
                jmax = j

    return imax, jmax


a = []
b = []

print("Введите размеры матрицы A:")
n = int(input("Количество строк: "))
m = int(input("Количество столбцов: "))

for i in range(n):
    row = []
    for j in range(m):
        x = int(input())
        row.append(x)
    a.append(row)

print("Введите размеры матрицы B:")
n2 = int(input("Количество строк: "))
m2 = int(input("Количество столбцов: "))

for i in range(n2):
    row = []
    for j in range(m2):
        x = int(input())
        row.append(x)
    b.append(row)

print("Исходная матрица A:", a)
print("Исходная матрица B:", b)

i1, j1 = find_max(a)
i2, j2 = find_max(b)

c = a[i1][j1]
a[i1][j1] = b[i2][j2]
b[i2][j2] = c

print("Преобразованная матрица A:", a)
print("Преобразованная матрица B:", b)
