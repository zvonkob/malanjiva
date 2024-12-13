import random
import string 


def get_word():
    with open('words.txt', 'r') as file:
        lines = file.readlines()
    return random.choice(lines).rstrip().lower()

def guessing_game(secret_word):
    open_word = len(secret_word) * ['_']
    print(''.join(open_word))
    zze = set()
    wrong_attempts = 0
    while True:
        letter = input('Enter a letter: ').lower()
        if len(letter) > 1:
            print('    Enter only one letter.')
        elif letter not in string.ascii_lowercase:
            print('    Enter only letters from a to z.')
        elif letter in zze:
            print('    You already guessed that letter.')
        else:
            zze.add(letter)
            if letter in secret_word:
                print('    Good guess')
                for i in range(len(secret_word)):
                    if secret_word[i] == letter:
                        open_word[i] = letter
            else:
                wrong_attempts += 1
                print(f'    Wrong guess ({wrong_attempts})')
                if wrong_attempts >= 6:
                    print(f'    Game over! The word was {secret_word}.')
                    break
            print('    '+ ''.join(open_word))
            if '_' not in open_word:
                print('    Congratulations! You guessed the word.')

def main():
    secret_word = get_word()
    print(secret_word)

    guessing_game(secret_word)

if __name__ == '__main__':
    main()