number = int(input())
result = 'Кораблей'

if number % 10 == 1 and number % 100 != 11:
    result = 'Корабль'
elif number % 10 >= 2 and number % 10 <= 4 and (number % 100 < 10 or number % 100 >= 20):
    result = 'Корабля'

print(result)