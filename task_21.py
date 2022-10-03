# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

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

int_in_input = []

for i in number:
    if not i.isdigit():
        continue
    if i.isdigit():
        int_in_input.append(i)
        summ_of_numbers += int(i)

print(f'Numbers in the entered number: {int_in_input}\nTheir sum = {summ_of_numbers}')