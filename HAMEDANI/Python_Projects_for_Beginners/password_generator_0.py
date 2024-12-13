import random


def get_password(n, uppercase, numbers, specials):
    lower = {chr(i) for i in range(ord('a'), ord('z') + 1)}
    upper = {chr(i) for i in range(ord('A'), ord('Z') + 1)}
    num = {chr(i) for i in range(ord('0'), ord('9') + 1)}
    spec = {'!', '#', '$', '%', '&', '?', '+', '=', '-'}
    universe = lower
    if uppercase: universe = universe.union(upper)
    if numbers: universe = universe.union(num)
    if specials: universe = universe.union(spec)
    universe = list(universe)
    print(sorted(universe))
    return ''.join([random.choice(universe) for i in range(n)])

def main():
    n = int(input('Enter password length: '))
    uppercase = input('Include uppercase letters? (y/n): ') == 'y'
    numbers = input('Include numbers? (y/n): ') == 'y'
    specials = input('Include special characters? (y/n):') == 'y'
    print(n, uppercase, numbers, specials)
    passw = get_password(n, uppercase, numbers, specials)

    print(passw)

if __name__ == '__main__':
    main()