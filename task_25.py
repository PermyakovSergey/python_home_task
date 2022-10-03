# Реализуйте алгоритм перемешивания списка.

from random import randint

size = 5
arr = []
for i in range(size):
    arr.append(randint(-100, 100))
print(arr)

arr_mix = list(set(arr))
print(arr_mix)

# СПАСИБО за подсказку, плохо конечно что удаляет "повторы", но
# через рекурсию тоже иногда "ломается" программа :)

# from random import randint

# size = 5
# arr = []
# for i in range(size):
#     arr.append(randint(0, 100))
# print(arr)
# arr_mixed = []
# arr_mixed.append(arr[(randint(1 , len(arr) - 1))])

# def mix_list(arr_in, arr_out):
#     if (len(arr_in) == len(arr_out)): print(arr_out)
#     else:
#         random_element = arr_in[(randint(0 , len(arr_in) - 1))]
#         if not random_element in arr_out:
#             arr_out.append(random_element)
#             mix_list(arr_in, arr_out)
#         else: mix_list(arr_in, arr_out)

# mix_list(arr, arr_mixed)