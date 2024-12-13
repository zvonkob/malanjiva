class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            return False
        self.balance -= amount
        return True

def read_positive_amount(prompt):
    while True:
        try:
            res = float(input(prompt))
            if res <= 0:
                raise ValueError('Amount must be positive')
            return number
        except ValueError:
            print('Please enter a valid number!')
            

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
            amount = atm.check_balance()
            print(f'Your current balance is :${amount:.2f}')            
        elif choice == '2':
            try:
                amount = read_positive_amount()
                atm.deposit(amount)
            except ValueError as ve:
                print(ve)
                break
            print(f'Successfully deposited ${amount:.2f}')
        elif choice == '3':
            try:
                amount = read_positive_amount()
                atm.withdraw(amount):
                print(f'Successfully withdrew ${amount:.2f}')
            except ValueError as ve:
                print(ve)
            else:
                print('Insufficient funds.')
        elif choice == '4':
            print('Thank you for using ATM.\n')
            break
        else:
            print('Please choose a number between 1 and 4!')

if __name__ == '__main__':
    main()