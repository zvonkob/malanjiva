import random


def main():
    while True:
        res = input('Roll the dice (y/n): ').lower()

        if res == 'y':
            i1 = random.randint(1, 6)
            i2 = random.randint(1, 6)
            print(f'({i1}, {i2})')
        elif res == 'n':
            print('Thanks for playing!')
            break
        else:
            print('Invalid choice!')


if __name__ == '__main__':
    main()