# В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, 
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

from random import randint

size = 10
start_num = randint(1, size)
lost_num = randint(1, size - 1)
with open('file.txt', 'w') as data: data.write(' '.join([str(start_num + i) for i in range(size + 1) if i != lost_num]))
with open('file.txt', 'r') as data: n_list = list(map(int, data.read().split()))
print((n_list), [(n_list[i-1] + 1) for i in range(1, len(n_list)) if n_list[i] - 1 != n_list[i-1]])

# num = 10
# rand_n = randint(1, 2)
# start_n = randint(1, 10)
# lost_num = randint(1, num - 1)
# str_nx = ''
# for i in range(num + 1):
#     if i != lost_num:
#         str_nx += str(start_n + i) + ' '
# with open('file.txt', 'w') as data: data.write(str_nx)

# with open('file.txt', 'r') as data: n_list = list(map(int, data.read().split()))
# print(n_list)
# for i in range(1, len(n_list)):
#     if n_list[i] - 1 != n_list[i-1]:
#         print(n_list[i-1] + 1)