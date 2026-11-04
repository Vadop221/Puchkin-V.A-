for k in range(3):
    n = int(input("Введите количество элементов массива: "))

    a = []

    for i in range(n):
        x = int(input())
        a.append(x)

    s = sum(a)
    sred = s / n

    print("Массив:", a)
    print("Сумма:", s)
    print("Среднее арифметическое:", sred)
