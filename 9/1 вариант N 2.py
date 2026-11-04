n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))

B = []

for i in range(n):
    row = list(map(int, input().split()))
    B.append(row)

print("Исходная матрица:")
for row in B:
    print(row)

for i in range(n):
    max_index = B[i].index(max(B[i]))
    min_index = B[i].index(min(B[i]))

    B[i][0], B[i][max_index] = B[i][max_index], B[i][0]

    min_index = B[i].index(min(B[i]))
    B[i][-1], B[i][min_index] = B[i][min_index], B[i][-1]

print("Полученная матрица:")
for row in B:
    print(row)
