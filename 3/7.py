def leap_year(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("Да")
    else:
        print("Нет")


year = int(input())

leap_year(year)
