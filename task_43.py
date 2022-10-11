# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся 
# элементов исходной последовательности.

my_list = list(str(11822355734))
for_comparison = list(set(my_list))
print((for_comparison))
res_list = []

for el in for_comparison:
    count = 0
    for i in range(len(my_list)):
        if my_list[i] == el:
            count +=1
    if count < 2:
        res_list.append(el)

print(res_list)