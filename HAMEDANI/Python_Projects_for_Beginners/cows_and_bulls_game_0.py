import random

def generate_unique_4():
    digits = list('123456789')
    g = random.choice(digits)
    number = g
    digits.remove(g)
    digits.append('0')
    for i in range(3):
        g = random.choice(digits)
        number += g
        digits.remove(g)
    return number

def validate_guess(secret_number, guess):
    cows, bulls = 0, 0
    for i in range(4):
        g = guess[i]
        if g in secret_number:
            if secret_number[i] == g:
                bulls += 1
            else:
                cows += 1
    return cows, bulls

def validate_guess_guess(secret_number, guess):
    bulls = sum([1 for i in range(4) if guess[i] == secret_number[i]])
    cows = sum([1 for i in range(4) if guess[i] in secret]) - bulls
    return cows, bulls
                
def main():
    secret_number = generate_unique_4()
    print(f'Secret number is {secret_number}\n')
    print('I have generated a 4-digit number with unique digits. Try to guess it!')

    while True:
        guess = input('Guess: ')
        if not (guess.isdecimal() and len(set(guess)) == 4):
            print('Invalid guess. Please enter 4-digit number with unique digits.')
            continue

        cows, bulls = validate_guess(secret_number, guess)
        print(f'{cows} cows, {bulls} bulls')

        if bulls == 4:
            print('Congratulations! You guessed the correct number.')
            return

if __name__ == '__main__':
    main()