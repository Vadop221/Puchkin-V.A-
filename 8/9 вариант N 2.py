for k in range(3):
    n = int(input("Введите количество элементов: "))

    a = []

    for i in range(n):
        x = int(input())
        a.append(x)

    p = 1

    for z in range(n):
        p = p * a[z]

    sred = sum(a) / n

    print("Массив:", a)
    print("Произведение:", p)
    print("Среднее арифметическое:", sred)
