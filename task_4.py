# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных 
# координат точек в этой четверти (x и y).

num_qarter = input('enter the number of the quarter of the coordinate plane: ')
while num_qarter not in ('1', '2', '3', '4'):
    print('wrong number of the quarter')
    num_qarter = input('enter the number of the quarter of the coordinate plane: ')
num_qarter = int(num_qarter)
if num_qarter == 1:
    print('x > 0 and y > 0')
elif num_qarter == 2:
    print('x < 0 and y > 0')
elif num_qarter == 3:
    print('x < 0 and y < 0')
elif num_qarter == 4:
    print('x > 0 and y < 0:')

