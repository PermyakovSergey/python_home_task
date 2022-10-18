# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

with open('poly_1.txt', 'w') as p_1: # для удобства :) с минусами не работает :(
    p_1.write('3x**8 + 31x**6 + x**4 + 91x**3 + 15x**2 + 39x + 40')
with open('poly_2.txt', 'w') as p_2:
    p_2.write('x**11 + 2x**8 + x**4 + 3x**2 + x + 1')

with open('poly_1.txt', 'r') as p1: unsort_sum = p1.read().split()
unsort_sum += '+'
with open('poly_2.txt', 'r') as p2: unsort_sum += p2.read().split()

unsort_sum = [item for item in unsort_sum if not '+' in item] # создаем список, состоящий из членов суммы многочленов

def get_deg(x):# возвращает строку, содержащую:
    if 'x**' in x:
        return str(x[x.index('x'):]) # основание с показателем степени, если у основания есть показатель
    elif 'x' in x and not '**' in x: return 'x' # основание, если нет степени
    else: return '' # пустую строку, если свободный член
def get_koef(x):# возвращает коэффициенты либо свободный член
    if 'x' in x and x.index('x') != 0: # если есть что-то до 'x', значит есть коэффициент
        return int(x[:x.index('x')]) # возвращаем коэффициент
    elif 'x' in x and x.index('x') == 0: return 1 # если перед 'x' ничего нет, значит коэф. = 1
    else: return int(x) # не содержит буквенной части, возвращаем свободный член
def for_max_deg(x):# для сортировки списка одночленов
    if 'x**' in x:
        return int(x[x.index('x') + 3:]) # возвращаем число после 'x**'
    elif 'x' in x and not '**' in x: return 1
    else: return 0

# сортирова списка одночленов от большей степени к меньшей - для вывода результата в стандартном виде
sort_sum = []
while (len(unsort_sum) > 0): # пока список не пустой (будут удаляться элементы, добавленные в результат)
    max_deg = max(for_max_deg(i) for i in unsort_sum) # присваивается максимальный показатель степени
    for i in range(len(unsort_sum)): # проходим по индексам несортированного списка одночленов
        if for_max_deg(unsort_sum[i]) == max_deg: # если степень элемента с индексом равна максимальной
            sort_sum.append(unsort_sum[i]) # добавит элемент с индексом в новый список
            del unsort_sum[i] # удалит добавленный элемент из несортированного списка
            break # чтобы не "list index out of range"
print(f'Sorted list: {sort_sum}')
# Нахождение подобных слагаемых и приведение к стандартному виду
res_str = ''
while (len(sort_sum) > 0): # будут удаляться элементы исходного списка после сравнения и записи результата
    num = sort_sum[0] # для сравнения берем 1й элемент списка
    comp = [get_deg(sort_sum[i]) for i in range(len(sort_sum)) if i != 0] # список (не) оснований (и их степеней) без num
    if get_deg(num) in comp: # если есть подобное слагаемое в сравниваемом списке,
        ind_c = comp.index(get_deg(num)) # получаем индекс подобного слагаемого в списке для сравнения,
        # далее в результат дозаписываем 'сумму коэффициентов подобных слагаемых' + 'слагаемое'
        res_str += \
            str(get_koef(num) + get_koef(sort_sum[ind_c + 1]))\
             + get_deg(num) + ' + '
        del sort_sum[ind_c + 1] # удаляем элемент, соответствующий подобному слагаемому - уже сложили в результат
    else: # если подобных слагаемых не найдено, добавляем в строку результата элемент списка одночленов
        res_str += num + ' + '
    del sort_sum[0] # удаляем, т.к. записан в результате
 
res_str = res_str[:-3] # запись результата без последнего '+'
print(f'res_str: {res_str}')
with open('poly_sum.txt', 'w') as poly_sum:
    poly_sum.write(res_str)