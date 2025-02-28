text_1 = 'Корабль'
text_2 = 'Корабля'
text_3 = 'Кораблей'

number = int(input())
result = text_3

if number % 10 == 1 and number % 100 != 11:
    result = text_1
elif number % 10 >= 2 and number % 10 <= 4 and (number % 100 < 10 or number % 100 >= 20):
    result = text_2

print(result)