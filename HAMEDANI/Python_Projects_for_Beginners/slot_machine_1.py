import emoji
import random

def get_starting_balance():
    while True:
        try:
            balance = int(input('Enter your starting balance: $'))
            if 0 < balance: 
                return balance
            print('Balance must be a positive number.')
        except ValueError:
            print('Please enter a valid number.')
   
def get_bet_amount(balance):
    while True:
        try:
            bet = int(input('Enter your bet amount: $'))
            if 1 < bet <= balance:
                return bet
            print('Invalid bet amount. ' + 
                  f'You can bet between $1 and ${balance}')
        except ValueError:
            print('Please enter a valid number for the bet amount.')

def spin_reels(bet):
    CHERRIES =   emoji.get_emoji_by_name(f':cherries:', 'en')
    LEMON =      emoji.get_emoji_by_name(f':lemon:', 'en')
    STAR =       emoji.get_emoji_by_name(f':star:', 'en')
    BELL =       emoji.get_emoji_by_name(f':bell:', 'en')
    WATERMELON = emoji.get_emoji_by_name(f':watermelon:', 'en')
    PICTURES = (CHERRIES, LEMON, STAR, BELL, WATERMELON)
    reel_1 = random.choice(PICTURES)
    reel_2 = random.choice(PICTURES)
    reel_3 = random.choice(PICTURES)
    print(f' {reel_1} | {reel_2} | {reel_3}')
    if reel_1 == reel_2 == reel_3:
        print(f'You won ${10 * bet}')
        return 10 * bet
    elif reel_1 == reel_2 or reel_1 == reel_3 or reel_2 == reel_3:
        print(f'You won ${2 * bet}')
        return 2 * bet
    else:
        print('You lost!')
        return 0

def main():

    balance = get_starting_balance()

    while True:
        print(f'\nCurrent balance: ${balance}')
       
        bet = get_bet_amount(balance)
           
        payout = spin_reels(bet)

        balance += payout - bet

        if balance < 0: break

        if input('Do you want to play again (y/n): ').lower() != 'y': break

    print('You are out of money! Game over.')

if __name__ == '__main__':
    main()