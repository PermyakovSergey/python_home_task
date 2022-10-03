# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

number = (input('enter the float number: '))
summ_of_numbers = 0

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

while not isfloat(number):
    number = (input('Wrong input, enter the float number: '))

for i in number:
    if not i.isdigit():
        continue
    if i.isdigit():
        summ_of_numbers += int(i)

print(summ_of_numbers)