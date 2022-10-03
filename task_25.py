# Реализуйте алгоритм перемешивания списка.

from random import randint

size = 5
arr = []
for i in range(size):
    arr.append(randint(-100, 100))
print(arr)

arr_mix = list(set(arr))
print(arr_mix) # СПАСИБО за подсказку, плохо конечно что удаляет "повторы" :)