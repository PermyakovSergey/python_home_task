# 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
#     *Пример:*
#     - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

print(dict(enumerate([3 * i + 1 for i in range(1, int(input('enter number: ')) + 1)], 1)))

# number = input('enter number: ')
# result = []
# for i in range(1, int(number) + 1):
#     result.append([i, 3 * i + 1])
# print(dict(result))