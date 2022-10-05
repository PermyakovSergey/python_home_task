# Задайте список из n чисел заполненный по формуле (1 + 1/n)**n и выведите 
# на экран их сумму.
# Пример:
# - Для n = 6: [2, 2, 2, 2, 2, 3] -> 13

n = 6

formula_list = []
sum_of_elements = 0
for i in range(1, n + 1):
    formula_list.append(round((1 + 1/i)**i))
    sum_of_elements += formula_list[i - 1]

print(f'Для n = {n}: {formula_list} -> {sum_of_elements}')

# Для словаря:

formula_dict = {}
sum_of_values = 0
for i in range(1, n + 1):
    formula_dict[i] = round(((1 + 1/i)**i), 2)
    sum_of_values += formula_dict[i]

print(f'Для n = {n} {formula_dict} -> {sum_of_values}')