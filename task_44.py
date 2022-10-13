# Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# сортируются единицы, нули, знак +, не записывается типа "1 = 0" и одночлены

from random import randint
import os

k = input('Enter the number > 0: ')
while not (k.isdigit() and int(k) > 0):
    k = input('Enter the number > 0: ')

nat_deg = int(k) # для работы, k сохраним для вывода
variable = 'x'

def rand_int(): return randint(0, 2) # для экспериментов с 0 и 1

with open('polynominal.txt', 'w') as data: # для очистки файла
    data.close()

while nat_deg > 0:
    rand_n = rand_int()
    if rand_n != 0 and os.stat("polynominal.txt").st_size != 0: # непонятное из интернета - помогло                                                                 
        with open('polynominal.txt', 'a') as data:              # не ставить плюс, если файл пустой :)
            data.write(f' + ')                                  # иногда получалcя результат типа "+ x = 0"
    if rand_n != 0: # если коэффициент не равен нулю что-нибудь запишет в файл
        with open('polynominal.txt', 'a') as data:
            if nat_deg > 0:
                if rand_n > 1: # 1x - некрасиво
                    data.write(f'{rand_n}')
                data.write(f'{variable}')
            if nat_deg > 1: # x**1 - тоже не красиво
                data.write(f'**{nat_deg}')
    if nat_deg == 1 and os.stat("polynominal.txt").st_size != 0: # добавит коэффициент без x, если ранее коэффициенты
        rand_n = rand_int()                      # не были равны нулю(файл не пустой), "1 = 0" не запишет в файл
        if rand_n != 0:
            with open('polynominal.txt', 'a') as data:
                data.write(f' + {rand_n}')
    nat_deg -= 1

# проверка: многочлен ли? Многочлен — это сумма одночленов, так что пример 10*x² = 0 - неверный
# и вывод результата
if os.stat("polynominal.txt").st_size == 0: # непонятное пригодилось еще раз :)
    print('Все коэффициенты равны нулю')
else:
    with open('polynominal.txt', 'r+') as data:
        result = data.read() # проверить строку на наличие '+'
        if '+' in result: # нет суммы - нет многочлена
            data.write(f' = 0') # сделаю как в примере, правда непонятно зачем
            data.close()
            with open('polynominal.txt', 'r') as data:
                print(f'Для k={k} => {data.read()}') # минимально возможный результат: x + 1 = 0
        else:
            print(f'результат: {result}\nне является многочленом, файл будет очищен')