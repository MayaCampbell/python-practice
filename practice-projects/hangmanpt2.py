import random
from words import words #from words.py imports variable words
import string

def find_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word
    return word.upper()

def hangman():
    #keeping track of letters and input
    word = find_valid_word(words)
    letter_in_word = set(words)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    while len(letter_in_word) > 0 and lives > 0:
        print('You have', lives, 'lives and have used these letters', ' '.join(used_letters))

        #word_list = [letter if letter in used_letters]

        word_list = []
        for letter in word:
            if letter in used_letters:
                word_list.append(letter)
            else:
                word_list.append('-')
        print("Current word: ", ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet not in used_letters:
            used_letters.add(user_letter)
            if user_letter in letter_in_word:
                letter_in_word.remove(user_letter)

            else:
                lives = lives - 1
                print("\nLetter is not in the word, lives = ", lives)

        elif user_letter in used_letters:
            print("\nSorry you have already guessed this letter")

        else:
            print("\nInvalid character. Please Try again")

    if lives == 0:
        print("Sorry you lost, the word was", word)
    else:
        print("Yay!! You guessed the word", word)


if __name__ == '__main__':
    hangman()

