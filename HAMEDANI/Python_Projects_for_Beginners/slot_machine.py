import random


def get_starting_balance():
    while True:
        try:
            balance = float(input('Enter your starting balance: $'))
            if 0 < balance: 
                break
            print('Balance must be a positive number.')
        except ValueError:
            print('Please enter a valid number.')
    return balance

def get_bet_amount(balance):
    while True:
        try:
            bet = float(input('Enter your bet amount: $'))
            if 1 < bet <= balance:
                break
            print('Invalid bet amount. ' + 
                  f'You can bet between $1 and ${balance:.2f}')
        except ValueError:
            print('Please enter a valid number for the bet amount.')
    return bet

def main():
    balance = get_starting_balance()

    while True:
        print(f'\nCurrent balance: ${balance:.2f}')
        bet = get_bet_amount(balance)
        

if __name__ == '__main__':
    main()