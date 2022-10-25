# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
#     *Пример:* 
#     - Для N = 5: 1, -3, 9, -27, 81

print([((-3)**i)//-3 for i in range(1, int(input('enter number: ')) + 1)])

# number = int(input('enter number: '))
# count = 1

# for i in range(number - 1):
#     count *= -3
#     print(count)