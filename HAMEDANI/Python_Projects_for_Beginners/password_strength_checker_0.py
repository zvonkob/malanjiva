def has_upper(name):
    for n in name:
        if n.isupper(): return True
    return False

def has_lower(name):
    for n in name:
        if n.islower(): return True
    return False

def has_special_character(name):
    specials = {'.', ';', '!', '?', '"', "'", '\\', '#'}
    for n in name:
        if n in specials: return True
    return False

def main():
    quality = {0: 'Very Weak', 1: 'Weak', 2: 'Medium',
               3: 'Strong', 4: 'Very Strong'}
    strength = 0
    password = input('Enter a password: ')

    if len(password) > 4: strength += 1
    if has_upper(password): strength += 1
    if has_lower(password): strength += 1
    if has_special_character(password) : strength += 1

    print(f'Password strength: {quality[strength]}' )

if __name__ == '__main__':
    main()