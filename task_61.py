# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся 
# элементов исходной последовательности.

my_list = list(map(int, str(11822355734)))
print(f'{my_list}\n{list(filter(lambda x: my_list.count(x) == 1, my_list))}')

# my_list = list(str(11822355734))
# print(my_list)

# for_comparison = list(set(my_list))
# res_list = []

# for el in for_comparison:
#     count = 0
#     for i in range(len(my_list)):
#         if my_list[i] == el:
#             count +=1
#     if count < 2:
#         res_list.append(el)

# print(res_list)