# Создайте программу для игры в ""Крестики-нолики"".

def show_field(matr):
    for line in matr:
        print(' '.join(line))
        print('-----------------')

def write_pos(pos, player, matr):
    for row in range(len(matr)):
        for col in range(len(matr)):
            if ((matr[row][col])[2]) == (pos): # Волшебная цифра 2 - индекс цифры в строке номера поля
                if player == 1:
                    matr[row][col] = '| X |'
                if player == 2:
                    matr[row][col] = '| 0 |'
    return matr

def check_win(player, matr):
    for i in range(len(matr)):
        temp = matr[i]
        if temp[0] == temp[1] == temp[2]:
            print(f'Winner is player {player}!')
            return True
        temp2 = []
        for j in range(len(matr)):
            temp2.append(matr[j][i])
    if temp2[0] == temp2[1] == temp2[2]:
        print(f'Winner is player {player}!')
        return True
    if matr[0][0] == matr[1][1] == matr[2][2] or matr[2][0] == matr[1][1] == matr[0][2]:
        print(f'Winner is player {player}!')
        return True
    else: return False

def start_game():
    field = [['| 1 |','| 2 |','| 3 |'],['| 4 |','| 5 |','| 6 |'],['| 7 |','| 8 |','| 9 |']]
    free_pos = ['1','2','3','4','5','6','7','8','9']
    while len(free_pos) > 0:
        for players in range(1, 3):
            show_field(field)
            pos_field = input(f'Player\'s {players} move! Choose number of field: ')
            while pos_field not in free_pos:
                pos_field = input('Choose free number of field: ')
            free_pos = list(filter(lambda x: x != pos_field, free_pos))
            field = write_pos(pos_field, players, field)

            if check_win(players, field):
                free_pos = []
                break
            if len(free_pos) == 0:
                print('Draw in the game!')
                break

start_game()