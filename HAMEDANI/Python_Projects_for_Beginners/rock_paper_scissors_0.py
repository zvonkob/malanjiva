import random
import emoji

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'

emoji_picture = {ROCK: emoji.get_emoji_by_name(':rock:', 'en'),
                 PAPER: emoji.get_emoji_by_name(':newspaper:', 'en'),
                 SCISSORS: emoji.get_emoji_by_name(':scissors:', 'en')}
epk = tuple(emoji_picture.keys())

while True:
    choice_me = input('Rock, paper, or scissors (r/p/s): ').lower()
    if choice_me in epk:
        print(f'You choose {emoji_picture[choice_me]:s}')
    else:
        print('Invalid choice!')
        continue

    choice_comp = random.choice(epk)    
    print(f'Computer choose {emoji_picture[choice_comp]:s}')

    if choice_me == choice_comp:
        print('Nobody wins')
    elif f'{choice_me}{choice_comp}' in {'rp', 'ps', 'sr'}:
        print('You lose')
    else:
        print('You win')

    if input('Continue (y/n) ').lower() == 'n':
        break

