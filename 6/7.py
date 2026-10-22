s = input("Введите строку: ")
n = len(s)

s1 = ""

for i in range(n):
    if i < n // 2 and s[i] == "п":
        s1 += "*"
    else:
        s1 += s[i]

print(s1)
