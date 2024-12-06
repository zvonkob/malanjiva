import random

min_int = int(input('Minimum integer: '))
max_int = int(input('Maximum integer: '))

number_to_guess = random.randint(min_int, max_int)

count= 0

while True:
    try:
        guess = int(input(f'Guess the number (between {min_int} and {max_int}): '))
        
        count += 1
        if guess < number_to_guess:
            print('Too low! Try again.')
        elif number_to_guess < guess:
            print('Too high! Try again.')
        else:
            print(f'Congratulations! You guessed the number in {count} attempts.')
            break
    except ValueError:
        print('Please enter a valid number')
