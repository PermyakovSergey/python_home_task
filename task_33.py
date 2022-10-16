# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

my_list = [1.1, 1.2, 3.1, 5, 10.01]
# result_list =[]
# for i in my_list:
#     if i % 1 != 0:
#         result_list.append(round(i % 1, 2))
# print(max(result_list) - min(result_list))

new_list = [(num % 1) for num in my_list if num % 1 != 0]
ins_list = [(num % 1) for num in my_list if isinstance(num, float)]
print(max(new_list) - min(new_list))
print(max(ins_list) - min(ins_list))

for i in my_list:
    print(isinstance(i, float))