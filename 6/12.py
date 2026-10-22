s = input("Введите текст: ")
words = s.lower().split()

for word in words:
    if word.endswith("я"):
        print(word)
