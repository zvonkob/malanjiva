import random
import string

def get_password(n, uppercase, numbers, specials):
    universe = string.ascii_lowercase
    password1 = []
    if uppercase:
        universe += string.ascii_uppercase
        must_uppercase = random.choice(list(string.ascii_uppercase))
        password1.append(must_uppercase)
        n -= 1
    if numbers:
        universe += string.digits
        must_numbers = random.choice(list(string.digits))
        password1.append(must_numbers)
        n -= 1
    if specials:
        universe += string.punctuation
        must_specials = random.choice(list(string.punctuation))
        password1.append(must_specials)
        n -= 1
    password2 = [random.choice(universe) for _ in range(n)]
    password = password1 + password2
    random.shuffle(password)
    return ''.join(password)

def main():
    n = int(input('Enter password length: '))
    uppercase = input('Include uppercase letters? (y/n): ').lower() == 'y'
    numbers = input('Include numbers? (y/n): ').lower() == 'y'
    specials = input('Include special characters? (y/n):').lower() == 'y'

    passw = get_password(n, uppercase, numbers, specials)

    print(passw)

if __name__ == '__main__':
    main()