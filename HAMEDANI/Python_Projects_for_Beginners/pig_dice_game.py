import random


def play_the_game(current_player):
    score = 0
    while True:
        n = random.randint(1, 6)
        if n == 1:
            score = 0
            break
        else:
            score += n
            print(f'You rolled a {n}')
            if input('Roll again? (y/n): ').lower() == 'n':
                break
    print(f'\nYou scored {score} points this turn.')
    return score


def main():
    current_score = [0, 0]
    current_player = 1
    while True:
        print(f'\nPlayer {current_player}\'s turn')
        score = play_the_game(current_player)
        current_score[current_player - 1] += score
        print(f'Current scores: Player 1: {current_score[0]}, Player 2: {current_score[1]}')
        if current_score[current_player - 1] >= 100:
            print(f'Player {current_score} wins!')
        current_player = 3 - current_player
    print()

if __name__ == '__main__':
    main()