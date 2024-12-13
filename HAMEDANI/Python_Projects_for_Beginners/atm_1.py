class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f'Your current balance is :${self.balance}')

    def deposit(self):
        while True:
            try:
                res = int(input('Enter the amount to deposit: $'))
                if 1 <= res:
                    print(f'Successfully deposited ${res}')
                    self.balance += res
                    break
                else:
                    print('Deposit amount must be positive.')
            except ValueError:
                print('Please enter a valid number.')

    def withdraw(self):
        while True:
            try:
                res = int(input('Enter the amount to withdraw: $'))
                if 1 <= res < self.balance:
                    print(f'Successfully withdrew ${res}')
                    self.balance -= res
                    break
                elif res >= self.balance:
                    print('Insufficient funds.')
                else:
                    print('Withdraw amount must be positive.')
            except ValueError:
                print('Please enter a valid number.')

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

def main():
    a = ATM()
    while True:
        choice = welcome_message()
        if choice == 1:
            a.check_balance()
        elif choice == 2:
            a.deposit()
        elif choice == 3:
            a.withdraw()
        elif choice == 4:
            break    

if __name__ == '__main__':
    main()