# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

my_list = [2, 3, 4, 5, 6]
print([(my_list[i] * my_list[-1 - i]) for i in range((len(my_list) + 1) // 2)])

# product_pairs = []
# for i in range((len(my_list) + 1) // 2): # + 1 - чтоб как в примере - перемножается элемент без пары сам на себя
#     product_pairs.append(my_list[i] * my_list[-1 - i])
# print(f'{my_list} => {product_pairs}')