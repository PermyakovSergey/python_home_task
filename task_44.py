# Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# Натуральной степенью числа a называется само это число, взятое n раз, 
# и умноженное само на себя. a n= a × a × ... × a n штук.

# очень долго мучился чтоб сортировались единицы, нули и знак +

from random import randint
import os

nat_deg = 3
variable = 'x'

def rand_int(): return randint(0, 1)

with open('polynominal.txt', 'w') as data:
    rand_n = 0
    print(f'first rand = {rand_n}')
    if rand_n != 0:
        if rand_n > 1:
            data.write(f'{rand_n}')
        data.write(f'{variable}')
        if nat_deg > 1:
            data.write(f'**{nat_deg}')
        nat_deg -= 1
        print(f'nat_deg = {nat_deg}')

while nat_deg > 0:

    rand_n = 0
    print(rand_n)
    if rand_n != 0 and os.stat("polynominal.txt").st_size != 0: # непонятно, но помогло не ставить плюс, если файл пустой :)
        with open('polynominal.txt', 'a+') as data:
            data.write(f' + ') 
    if rand_n != 0:
        with open('polynominal.txt', 'a') as data:
            if nat_deg > 0:
                if rand_n > 1:
                    data.write(f'{rand_n}')
                data.write(f'{variable}')
            if nat_deg > 1:
                data.write(f'**{nat_deg}')
    # nat_deg -= 1
    if nat_deg == 1 and os.stat("polynominal.txt").st_size != 0:
        rand_n = rand_int()
        print(f'end r = {rand_n}')
        if rand_n != 0:
            with open('polynominal.txt', 'a') as data:
                data.write(f' + {rand_n}')
    nat_deg -= 1

if os.stat("polynominal.txt").st_size != 0:
    with open('polynominal.txt', 'a') as data:
        data.write(f' = 0')
