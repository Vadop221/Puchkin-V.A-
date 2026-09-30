seconds = int(input("Введите количество секунд: "))

days = seconds // 86400
seconds = seconds % 86400

hours = seconds // 3600
seconds = seconds % 3600

minutes = seconds // 60
seconds = seconds % 60

print("Дней:", days)
print("Часов:", hours)
print("Минут:", minutes)
print("Секунд:", seconds)
