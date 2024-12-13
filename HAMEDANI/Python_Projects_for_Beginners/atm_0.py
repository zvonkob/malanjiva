def welcome_message():
    print('\nWelcome to the ATM!')
    print('1. Check Balance')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Exit')
    while True:
        try:
            res = int(input('Please choose an option: '))
            if 1 <= res <= 4:
                return res
        except ValueError:
            print('Please choose a number!')

def check_balance(balance):
    print(f'Your current balance is :{balance}')

def deposit(balance):
    while True:
        try:
            res = int(input('Enter the amount to deposit: '))
            if 1 <= res:
                print(f'Successfully deposited ${res}')
                return balance + res
            else:
                print('Deposit amount must be positive.')
        except ValueError:
            print('Please enter a valid number.')

def withdraw(balance):
    while True:
        try:
            res = int(input('Enter the amount to withdraw: '))
            if 1 <= res < balance:
                print(f'Successfully withdraw ${res}')
                return balance - res
            elif res >= balance:
                print('Insufficient funds.')
            else:
                print('Withdraw amount must be positive.')
        except ValueError:
            print('Please enter a valid number.')

def main():
    balance = 0
    while True:
        choice = welcome_message()
        if choice == 1:
            check_balance(balance)
        elif choice == 2:
            balance = deposit(balance)
        elif choice == 3:
            balance = withdraw(balance)
        elif choice == 4:
            break    

if __name__ == '__main__':
    main()