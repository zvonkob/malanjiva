import emoji
import random

CHERRIES =   emoji.get_emoji_by_name(f':cherries:', 'en')
LEMON =      emoji.get_emoji_by_name(f':lemon:', 'en')
STAR =       emoji.get_emoji_by_name(f':star:', 'en')
BELL =       emoji.get_emoji_by_name(f':bell:', 'en')
WATERMELON = emoji.get_emoji_by_name(f':watermelon:', 'en')

PICTURES = (CHERRIES, LEMON, STAR, BELL, WATERMELON)

def get_starting_balance():
    while True:
        try:
            balance = int(input('Enter your starting balance: $'))
            if 0 < balance: 
                break
            print('Balance must be a positive number.')
        except ValueError:
            print('Please enter a valid number.')
    return balance

def get_bet_amount(balance):
    while True:
        try:
            bet = int(input('Enter your bet amount: $'))
            if 1 < bet <= balance:
                break
            print('Invalid bet amount. ' + 
                  f'You can bet between $1 and ${balance}')
        except ValueError:
            print('Please enter a valid number for the bet amount.')
    return bet

def play_slot_machine(balance, bet):
    reel_1 = random.choice(PICTURES)
    reel_2 = random.choice(PICTURES)
    reel_3 = random.choice(PICTURES)
    print(f' {reel_1} | {reel_2} | {reel_3}')
    if reel_1 == reel_2 == reel_3:
        print(f'You won ${10 * bet}')
        return balance - bet + 10 * bet
    elif reel_1 == reel_2 or reel_1 == reel_3 or reel_2 == reel_3:
        print(f'You won ${2 * bet}')
        return balance - bet + 2 * bet
    else:
        print('You lost!')
        return balance - bet

def main():

    print(PICTURES)

    balance = get_starting_balance()

    while balance > 0:
        print(f'\nCurrent balance: ${balance}')
       
        bet = get_bet_amount(balance)
           
        balance = play_slot_machine(balance, bet)

        if input('Do you want to play again (y/n): ').lower() != 'y': break

    print('You are out of money! Game over.')

if __name__ == '__main__':
    main()