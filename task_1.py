# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот 
# день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

number = int(input('enter the number of the week day: '))

if number == 1:
    print('no')
elif number == 2:
    print('no')
elif number == 3:
    print('no')
elif number == 4:
    print('no')
elif number == 5:
    print('no')
elif number == 6:
    print('yes')
elif number == 7:
    print('yes')
else:
    print('wrong number of day')
