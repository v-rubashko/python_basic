year = int(input('Введите год для проверки на високосность: '))

is_leap_year = True if year % 400 == 0 or year % 100 != 0 and year % 4 == 0 else False

print(is_leap_year)
