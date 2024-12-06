import random


best_score = 10000
while True:
    number_to_guess = random.randint(1, 100)
    count= 0
    while True:
        try:
            guess = int(input('Guess the number (between 1 and 100): '))
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
    if count < best_score:
        best_score = count
    print(f'Best score: {best_score}')