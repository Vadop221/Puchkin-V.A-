s = input("Введите строку: ")
con = s.count("а")

s = s.replace("а", "о")

print(s)
print("Количество замен:", con)
print("Количество символов:", len(s))
