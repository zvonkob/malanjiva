import random

def roll_die():
    return random.randint(1, 6)

def play_turn(player_name):
    turn_score = 0

    print(f"{player_name}'s turn")

    while True:
        roll = roll_die()
        print(f'You rolled a {roll}')

        if roll == 1:
            return 0
        
        turn_score += roll
        choice = input('Roll again? (y/n): ').lower()
        if choice != 'y':
            return turn_score

def main():
    scores = [0, 0]
    current_player = 0

    while True:
        player_name = f'Player {current_player + 1}'
        play_turn(player_name)


if __name__ == '__main__':
    main()