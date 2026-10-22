s = input("Введите строку: ")

con = 0
max_con = 0

for char in s:
    if char == "н":
        con += 1
        if con > max_con:
            max_con = con
    else:
        con = 0

s = s.replace("!", ".")

print("Самая длинная последовательность н:", max_con)
print(s)
