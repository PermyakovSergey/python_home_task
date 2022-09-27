# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот 
# день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

number = input('enter the number of the week day: ')
while number not in ('1', '2', '3', '4', '5', '6', '7'):
    print('there is no such day of the week')
    number = input('enter the number of the week day: ')
number = int(number)
if number > 0 and number < 6:
    print('no')
else:
    print('yes')