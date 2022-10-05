# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

from math import pow

def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    else: return fib(n - 1) + fib(n - 2)

def fib_neg(n):
    if n == 0: return 0
    if n == 1: return 1
    else: return fib_neg(n + 2) - fib_neg(n + 1)

k = 8
f_list = []

for i in range(k+1):
    if i != 0: # чтобы не было двух нулей
        f_list.insert(0, fib_neg(-i))
    f_list.append(fib(i))

print(f_list)
