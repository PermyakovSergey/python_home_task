# Задайте список из n чисел заполненный по формуле (1 + 1/n)**n и выведите 
# на экран их сумму.
# Пример:
# - Для n = 6: [2, 2, 2, 2, 2, 3] -> 13

n = 6

formula_list = []
for i in range(1, n + 1):
    formula_list.append(round((1 + 1/i)**i))

sum_of_elements = 0
for i in formula_list:
    sum_of_elements += i
print(f'Для n = {n}: {formula_list} -> {sum_of_elements}')
