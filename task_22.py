# Напишите программу, которая принимает на вход число N и выдает набор 
# произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


number = input('enter the number > 0: ')
while not (number.isdigit() and int(number) != 0):
    number = input('Wrong input, enter the number > 0: ')
number = int(number)

product = 1
text = '1'
comment = [1,]
product_set = []

for i in range(1, number + 1):
    product *= i
    product_set.append(product)
    if i < number:
        text = text + '*' + str(i + 1)
        comment.append(text)

like_in_example = tuple(comment) # чтоб c круглыми скобками и без кавычек :)
like_in_example = str(like_in_example)
like_in_example = str(like_in_example.replace('\'', ''))
print(f'набор произведений чисел от 1 до N:\n{product_set} {like_in_example}')