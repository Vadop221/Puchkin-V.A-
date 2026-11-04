s = input("Введите строку: ")

words = s.split()

result = []

for word in words:
    new_word = ''.join(sorted(word))
    result.append(new_word)

print(' '.join(result))
