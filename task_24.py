# новое условие:
# Напишите программу, которая на вход принимает два числа. Задайте список из N элементов, заполненных
# числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# - 15

number_of_el = 5

first_pos = input(f'enter the first number from 1 to {number_of_el}: ')
while not (first_pos.isdigit() and int(first_pos) in range(1, (number_of_el + 1))):
    first_pos = input(f'Wrong input, enter the first number from 1 to {number_of_el}: ')
first_pos = int(first_pos)

second_pos = input(f'enter the second number from 1 to {number_of_el}: ')
while not (second_pos.isdigit() and int(second_pos) in range(1, (number_of_el + 1))):
    second_pos = input(f'Wrong input, enter the second number from 1 to {number_of_el}: ')
second_pos = int(second_pos)

list_of_el = []
for i in range(-number_of_el, number_of_el + 1):
    list_of_el.append(i)

print(
    f'Position one: {first_pos}\n' +
    f'Position two: {second_pos}\n' +
    f'Number of elements: {number_of_el} or {number_of_el*2 + 1}?\n' +
    f'{list_of_el}\n'
    f'{list_of_el[first_pos - 1] * list_of_el[second_pos - 1]}'
)

# Старое условие:
# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

# from random import randint

# n = input('enter the number N > 0: ')
# while not (n.isdigit() and int(n) > 0):
#     n = input('enter the number N > 0: ')
# n = int(n)
# arr_n = []
# for i in range(n):
#     arr_n.append(randint(-n, n))
# print(f'список из {n} элементов: {arr_n}')

# positions = []

# if n == 1:
#     with open('file.txt', 'w') as data:
#         data.write(f'{0}')
#         positions.append(0)
# elif n < 4:
#     with open('file.txt', 'w') as data:
#         for i in range(len(arr_n) - 1):
#             positions.append(i)
#             data.write(f'{i}\n')
# else:
#     with open('file.txt', 'w') as data:
#         for i in range(0, len(arr_n), 2):
#             positions.append(i)
#             data.write(f'{i}\n')

# product = 1
# with open('file.txt', 'r') as data:
#     for line in data:
#         product *= arr_n[int(line)]

# print(f'произведение элементов на позициях: {positions} = {product}')