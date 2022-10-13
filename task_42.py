# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = 650
list_of_mults = []
if number == 1: list_of_mults.append(number)
while number != 1:
    for simple_mult in range(2, number + 1):
        if number % simple_mult == 0:
            list_of_mults.append(simple_mult)
            break
    number = number // simple_mult

print(list_of_mults)