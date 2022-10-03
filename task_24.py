# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint

n = input('enter the number N > 0: ')
while not (n.isdigit() and int(n) > 0):
    n = input('enter the number N > 0: ')
n = int(n)
arr_n = []
for i in range(n):
    arr_n.append(randint(-n, n))
print(f'список из {n} элементов: {arr_n}')

positions = []

if n == 1:
    with open('file.txt', 'w') as data:
        data.write(f'{0}')
        positions.append(0)
elif n < 4:
    with open('file.txt', 'w') as data:
        for i in range(len(arr_n) - 1):
            positions.append(i)
            data.write(f'{i}\n')
else:
    with open('file.txt', 'w') as data:
        for i in range(0, len(arr_n), 2):
            positions.append(i)
            data.write(f'{i}\n')

product = 1
with open('file.txt', 'r') as data:
    for line in data:
        product *= arr_n[int(line)]

print(f'произведение элементов на позициях: {positions} = {product}')