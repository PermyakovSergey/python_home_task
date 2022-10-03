# Напишите программу, которая принимает на вход число N и выдает набор 
# произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ]

number = input('enter the number > 0: ')
while not (number.isdigit() and int(number) != 0):
    number = input('Wrong input, enter the number > 0: ')
number = int(number)

product = 1
product_set = []

for i in range(1, number + 1):
    product *= i
    product_set.append(product)

print(product_set)