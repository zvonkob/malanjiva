def print_board(bb):
    print('---+---+---')
    for b in bb:
        print(f' {b[0]} | {b[1]} | {b[2]}\n---+---+---')
              
def get_row_or_column(label):
    while True:
        try:
            n = int(input((f'Enter {label} (0-2): ')))
            if n < 0 or 2 < n: raise ValueError()
            return n
        except ValueError: print('Invalid input!')

def get_row_and_column(board):
    while True:
        i = get_row_or_column('row')
        j = get_row_or_column('column')
        if board[i][j] == ' ': return i, j
        print('This spot is already taken')

def three_in_a_row(current_player, board):
    x = [[1 if board[i][j] == current_player else 0 
            for j in range(3)] for i in range(3)]
    for i in range(3):
        if sum([x[i][j] for j in range(3)]) == 3: return True
    for j in range(3):
        if sum([x[i][j] for i in range(3)]) == 3: return True
    if sum([x[k][k] for k in range(3)]) == 3: return True
    if sum([x[2-k][k] for k in range(3)]) == 3: return True
    return False

def is_full_board(bb):
    for b in bb:
        if ' ' in b:
            return False
    return True

def play_tic_tac_toe(current_player, board):
    while True:
        print(f'Player {current_player}\'s turn')

        i, j = get_row_and_column(board)
        board[i][j] = current_player
        print_board(board)

        if three_in_a_row(current_player, board):
            print(f'Player {current_player} wins!'); break

        if is_full_board(board):
            print('The board is full!'); break

        current_player = 'O' if current_player == 'X' else 'X'

def main():
    board = [[' '] * 3 for i in range(3)]
    print_board(board)
    current_player = 'X'
    play_tic_tac_toe(current_player, board)

if __name__ == '__main__':
    main()