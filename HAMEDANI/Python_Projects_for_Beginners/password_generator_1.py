import random
import string

def get_password(n, uppercase, numbers, specials):
    universe = string.ascii_lowercase
    if uppercase:
        universe += string.ascii_uppercase
    if numbers:
        universe += string.digits
    if specials:
        universe = string.punctuation
    return ''.join([random.choice(universe) for i in range(n)])

def main():
    n = int(input('Enter password length: '))
    uppercase = input('Include uppercase letters? (y/n): ').lower() == 'y'
    numbers = input('Include numbers? (y/n): ').lower() == 'y'
    specials = input('Include special characters? (y/n):').lower() == 'y'
    print(n, uppercase, numbers, specials)

    passw = get_password(n, uppercase, numbers, specials)

    print(passw)

if __name__ == '__main__':
    main()