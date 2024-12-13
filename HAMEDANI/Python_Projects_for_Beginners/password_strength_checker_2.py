import re

def check_password_strength(password)
    quality = {0: 'Very Weak', 1: 'Weak', 2: 'Medium',
               3: 'Strong', 4: 'Very Strong'}
    strength = 0
    if len(password) > 8: strength += 1
    if re.search('[A-Z]', password): strength += 1
    if re.search('[a-z]', password): strength += 1
    if re.search('[0-9]', password): strength += 1
    if re.search('[!?;.#$%&/]', password): strength += 1
    return quality[strength]

def main():
    password = input('Enter a password: ')
    strength = check_password_strength(password)
    print(f'Password strength: {strength}' )

if __name__ == '__main__':
    main()