# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input('Enter an integer: ')) 
temp_number = ''
while number != 0:
    temp_number += str(number % 2)
    number = number // 2

bin_num = ''
for i in range(len(temp_number)):
    bin_num += temp_number[-i-1]
print(f'Number in binary -> {bin_num}')
