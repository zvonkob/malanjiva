import random


number_to_guess = random.randint(1, 100)
number_to_guess_max = 3

count = 0

while True:
    try:
        guess = int(input('Guess the number (between 1 and 100): '))
        
        count += 1
        if count > number_to_guess_max:
            print(f'End of the game: more than {number_to_guess_max} attempts')
            print()
            print(f'Number to guess was: {number_to_guess}')
            break
        else:
            if guess < number_to_guess:
                print('Too low! Try again.')
            elif number_to_guess < guess:
                print('Too high! Try again.')
            else:
                print(f'Congratulations! You guessed the number in {count} attempts.')
                break
    except ValueError:
        print('Please enter a valid number')
