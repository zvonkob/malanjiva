import emoji
import random


KAMEN = 'r'
PAPER = 'p'
SCISSORS = 's'
emojis = {KAMEN: emoji.get_emoji_by_name(':KAMEN:', 'en'),
          PAPER: emoji.get_emoji_by_name(':newspaper:', 'en'),
          SCISSORS: emoji.get_emoji_by_name(':scissors:', 'en')}
choices = tuple(emojis.keys())

def get_user_choice():
    while True:
        user_choice = input('KAMEN, paper, scissors? (r/p/s): ').lower()
        if user_choice in choices:
            return user_choice
        else:
            print('Invalid choice!')

def display_choices(user_choice, computer_choice):
    print(f'You chose {emojis[user_choice] }')
    print(f'Computer chose {emojis[computer_choice]}')

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('It\'s a tie!')
    elif (
            (user_choice == KAMEN and computer_choice == SCISSORS) or
            (user_choice == SCISSORS and computer_choice == PAPER) or
            (user_choice == PAPER and computer_choice == KAMEN)):
        print('You win')
    else:
        print('You lose')

def play_game():
    while True:
        user_choice  = get_user_choice()

        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)

        if input('Continue (y/n): ').lower() == 'n':
            break

play_game()