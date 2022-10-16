# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

res_pol = ''

with open('poly_1.txt', 'r') as p1:
    res_pol = p1.read()
res_pol += ' + '
with open('poly_2.txt', 'r') as p2:
    res_pol += p2.read()

print(res_pol)