s = input("Введите текст: ")
words = s.lower().split()

for word in words:
    if word.startswith("а") or word.endswith("я"):
        print(word)
