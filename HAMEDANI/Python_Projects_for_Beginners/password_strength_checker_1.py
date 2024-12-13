import re

def main():
    quality = {0: 'Very Weak', 1: 'Weak', 2: 'Medium',
               3: 'Strong', 4: 'Very Strong'}
    strength = 0
    password = input('Enter a password: ')

    if len(password) > 4: strength += 1
    if re.search('[A-Z]', password): strength += 1
    if re.search('[a-z]', password): strength += 1
    if re.search('[!?;.#$%&/]', password): strength += 1

    print(f'Password strength: {quality[strength]}' )

if __name__ == '__main__':
    main()