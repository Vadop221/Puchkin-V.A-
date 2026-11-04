n = int(input("Введите размер матрицы: "))

A = [[0] * n for i in range(n)]

top = 0
bottom = n - 1
left = 0
right = n - 1

num = 1

while top <= bottom and left <= right:

    for j in range(left, right + 1):
        A[top][j] = num
        num += 1
    top += 1

    for i in range(top, bottom + 1):
        A[i][right] = num
        num += 1
    right -= 1

    if top <= bottom:
        for j in range(right, left - 1, -1):
            A[bottom][j] = num
            num += 1
        bottom -= 1

    if left <= right:
        for i in range(bottom, top - 1, -1):
            A[i][left] = num
            num += 1
        left += 1

print("Матрица по спирали:")
for row in A:
    print(*row)
