import random


def main():
    n = int(input('How many dice? '))

    count = 0
    while True:
        res = input('Roll the dice (y/n): ').lower()

        if res == 'y':
            count += 1
            ii = [random.randint(1, 6) for i in range(n)]
            print()
            print(count, ii)
        elif res == 'n':
            print('Thanks for playing!')
            break
        else:
            print('Invalid choice!')


if __name__ == '__main__':
    main()