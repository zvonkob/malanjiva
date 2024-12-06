import emoji
import random

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'

emojis = {ROCK: emoji.get_emoji_by_name(':rock:', 'en'),
          PAPER: emoji.get_emoji_by_name(':newspaper:', 'en'),
          SCISSORS: emoji.get_emoji_by_name(':scissors:', 'en')}
choices = tuple(emojis.keys())

while True:
    user_choice = input('Rock, paper, scissors? (r/p/s): ').lower()
    if user_choice not in choices:
        print('Invalid choice!')
        continue

    computer_choice = random.choice(choices)

    print(f'You chose {emojis[user_choice] }')
    print(f'Computer chose {emojis[computer_choice]}')

    if user_choice == computer_choice:
        print('It\'s a tie!')
    elif (
            (user_choice == ROCK and computer_choice == SCISSORS) or
            (user_choice == SCISSORS and computer_choice == PAPER) or
            (user_choice == PAPER and computer_choice == ROCK)):
        print('You win')
    else:
        print('You lose')

    if input('Continue (y/n): ').lower() == 'n':
        break

