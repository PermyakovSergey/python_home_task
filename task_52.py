# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint

candyes = 2021

player_name = (input('Please enter your name: '))

# кусок кода для жеребьевки.
def turn():
    num = (input('Please enter 0 or 1: '))
    while not (num.isdigit() and num in ['0', '1']):
        num = (input('Please enter 0 or 1: '))
    rand = randint(0, 1)
    print(f'random number = {rand}, yours number = {num}')
    if rand == int(num):
        print(f'You guessed a random number, the first move is yours!')
        return 1
    else:
        print(f'You did not guess the number, the bot goes first!')
        return 0
k = turn()

print('In one move, you can pick up no more than 28 candies\n')

while candyes > 28:
    for players in range(1, 3):

        if k == 0: # Включить для жеребьевки
            k = 1
            continue

        if players == 1:
            takes = input(f'{player_name} takes: ')
            while not (takes.isdigit() and 0 < int(takes) < 29):
                takes = input(f'The number should be from 1 to 28\n{player_name} takes: ')
        if players == 2:
            # var 1: hard??? :)
            if (candyes - (candyes // 28)*28) == 0: takes = 28
            else: takes = (candyes - (candyes // 28)*28)
            # var 2:
            # if candyes % 2:
            #     takes = 27
            # else: takes = 28

            if 58 < candyes <= 86: # Я даже у такого без калькулятора не выиграю :)
                print('Looks like I Won')
                takes = candyes - 58

            if candyes < 58: # Это оставить - норм :)
                takes = candyes - 29
            if candyes == 29:
                print('Looks like I lost')
                takes = randint(1, 29)
            print(f'bot takes: {takes}')
        candyes -= int(takes)

        if candyes < 29:
            if players == 2: players = player_name
            else: players = 'Skynet'
            print(f'\nThe remaining {candyes} candies are taken by the {players}, {players} won!\n')
            break
        print(f'there are {candyes} candies left\n')

# candyes = 58
# print('За один ход можно забрать не более чем 28 конфет')
# while candyes > 0:
#     for players in range(1, 3):
#         takes = input(f'{players} player takes: ')
#         while not (takes.isdigit() and 0 < int(takes) < 29):
#             takes = input(f'{players} player takes: ')
#         candyes -= int(takes)
#         if candyes < 1:
#             print(f'Player {players} won')
#             break
#         print(f'there are {candyes} candies left')