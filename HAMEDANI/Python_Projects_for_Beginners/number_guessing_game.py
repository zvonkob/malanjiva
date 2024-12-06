import random


number_to_guess = random.randint(1, 100)

count= 0

while True:
    try:
        guess = int(input('Guess the number (between 1 and 100): '))

        if guess < number_to_guess:
            print('Too low! Try again.')
        elif number_to_guess < guess:
            print('Too high! Try again.')
        else:
            print(f'Congratulations! You guessed the number in {count} attempts.')
            break
        count += 1
    except ValueError:
        print('Please enter a valid number')



