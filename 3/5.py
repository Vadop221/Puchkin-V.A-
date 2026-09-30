def minimum(a, b, c):
    if a <= b and a <= c:
        print(a)
    elif b <= a and b <= c:
        print(b)
    else:
        print(c)


a = int(input())
b = int(input())
c = int(input())

minimum(a, b, c)
