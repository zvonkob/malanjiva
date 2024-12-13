class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f'Your current balance is :${self.balance:.2f}')

    def deposit(self, amount):
        self.balance += amount
        print(f'Successfully deposited ${amount:.2f}')

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            print(f'Successfully withdrew ${amount:.2f}')
        else:
            print('Insufficient funds.')

def read_positive_amount():
    while True:
        try:
            res = float(input('Enter the amount: $'))
            if 1 <= res:
                return res
            else:
                print('Amount must be positive and greater than $1.00.')
        except ValueError:
            print('Please enter a valid number.')

def main():
    atm = ATM()
    while True:
        print('\nWelcome to the ATM!')
        print('1. Check Balance')
        print('2. Deposit')
        print('3. Withdraw')
        print('4. Exit')
        choice = input('Please choose an option: ')
        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            amount = read_positive_amount()
            atm.deposit(amount)
        elif choice == '3':
            amount = read_positive_amount()
            atm.withdraw(amount)
        elif choice == '4':
            print('Thank you for using ATM.\n')
            break
        else:
            print('Please choose a number between 1 and 4!')

if __name__ == '__main__':
    main()