def draw_board(table):
    grablje = '---+---+---'
    print(grablje)
    for i in range(3):
        j, k, l = table[i]
        print(f' {j} | {k} | {l} ')
        print(grablje)
              
def get_row_or_column(label):
    while True:
        try:
            n = int(input((f'Enter {label} (0-2): ')))
            if n < 0 or 2 < n: raise ValueError()
            return n
        except ValueError: print('Invalid input!')

def get_row_and_column(table):
    while True:
        i = get_row_or_column('row')
        j = get_row_or_column('column')
        if table[i][j] == ' ': return i, j
        print('This spot is already taken')

def three_in_a_row(player, tab):
#    itable = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#    for i in range(3):
#       for j in range(3):
#           if table[i][j] == player: itable[i][j] = 1
    x = [[1 if tab[i][j] == player else 0 for j in range(3)] for i in range(3)]
    for i in range(3):
        if sum([x[i][j] for j in range(3)]) == 3: return True
    for j in range(3):
        if sum([x[i][j] for i in range(3)]) == 3: return True
    if sum([x[k][k] for k in range(3)]) == 3: return True
    if sum([x[2-k][k] for k in range(3)]) == 3: return True
    return False

def play_tic_tac_toe(player, table):
    count = 0
    while True:
        print(f'Player {player}\'s turn')
        i, j = get_row_and_column(table)
        count += 1
        table[i][j] = player
        draw_board(table)
        if three_in_a_row(player, table):
            print(f'Player {player} wins!'); break
        player = 'O' if player == 'X' else 'X'
        if count == 9:
            print('The board is full!'); break

def main():
    table = [[' '] * 3 for i in range(3)]
    player = 'X'
    play_tic_tac_toe(player, table)

if __name__ == '__main__':
    main()