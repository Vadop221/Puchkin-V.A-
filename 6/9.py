s = input("Введите текст: ").lower()
word = input("Введите искомое слово: ").lower()

words = s.split()
con = words.count(word)

print(con)
