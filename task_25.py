# Реализуйте алгоритм перемешивания списка.

from random import randint

size = 5
arr = []
for i in range(size):
    arr.append(randint(0, 100))
print(arr)
arr_m = []
arr_m.append(arr[(randint(1 , len(arr) - 1))])

def func(arr1, arr2):
    if (len(arr1) == len(arr2)): print(arr2)
    else:
        r = arr1[(randint(0 , len(arr1) - 1))]
        if not r in arr2:
            arr2.append(r)
            func(arr1, arr2)
        else: func(arr1, arr2)

func(arr, arr_m)
