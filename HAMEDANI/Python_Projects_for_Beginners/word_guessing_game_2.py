import random
import string 


def read_words():
    try:
        with open('words.txt', 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print('words.txt does not exist.')
        return []

def get_letter(guessed_letters):
    while True:
        letter = input('Enter a letter: ').lower()
        if len(letter) > 1:
            print('    Enter only one letter.')
        elif letter not in string.ascii_lowercase:
            print('    Enter only letters from a to z.')
        elif letter in guessed_letters:
            print('    You already guessed that letter.')
        else: 
            return letter

def display_word(secret_word, guessed_letters):
    word_to_display = ''
    underscores = False
    for letter in secret_word:
        if letter in guessed_letters:
            word_to_display += letter
        else:
            word_to_display += '_'
            underscores = True
    print(word_to_display)
    return underscores

def guessing_game(secret_word):
    guessed_letters = set()
    wrong_attempts = 0
    while True:
        letter = get_letter(guessed_letters)
        if letter in secret_word:
            print('    Good guess')
            guessed_letters.add(letter)
            underscores = display_word(secret_word, guessed_letters)
            if not underscores:
                print('    Congratulations! You guessed the word.')
                return
        else:
            wrong_attempts += 1
            print(f'    Wrong guess ({wrong_attempts})')
            if wrong_attempts > 6:
                print(f'    Game over! The word was {secret_word}.')

def main():
    words = read_words()
    if not words:
        print('No words loaded.'); return

    secret_word = random.choice(words)
    print(secret_word)

    guessing_game(secret_word)

if __name__ == '__main__':
    main()