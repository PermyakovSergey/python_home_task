# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример: На сжатие входные данные: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Выходные данные: 12W1B12W3B24W1B14W

with open('data_in.txt', 'r') as in_data:
    data_in = in_data.read()

data_in += '-' # чтобы не 'string index out of range' и перебрать всю исходную строку
compressed_data = ''
count = 1

for i in range(len(data_in) - 1):
    if data_in[i] == data_in[i + 1]:
        count += 1
    else:
        compressed_data += str(count) + data_in[i]
        count = 1
print(f'compressed_data: {compressed_data}')

with open('compressed_data.txt', 'w') as data_comp:
    data_comp.write(compressed_data)

recovered_data = ''
num = ''

for i in range(len(compressed_data)):
    if compressed_data[i].isdigit():
        num += compressed_data[i]
    else:
        recovered_data += compressed_data[i]*int(num)
        num = ''
print(f'recovered_data: {recovered_data}')