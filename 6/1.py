s = input("Введите текст: ")
words = s.lower().split()
con = 0

for word in words:
    if word.startswith("е"):
        con += 1

print(con)
