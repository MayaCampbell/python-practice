import random
from words import words
import string

#print(words)

def get_valid_word(words):
    word = random.choice(words) #set variable word to random.choice(words)-- chooses something randomly from the list
    while "-" in words or " " in words: # make sure no "-" or " " spaces in the word
        word #if while loop false choose again
        
    return word.upper() #return (hold) valid word .upper() to make the word uppercase

def hangman():
    word = get_valid_word(words) #word variable is set to word returned from above function
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase) #letters from the alphabet
    used_letters = set() #letters already used
    lives = 7

    #getting user input
    while len(word_letters) > 0 and lives > 0:
        #letters used
        print('You have', lives ,'lives left and you have used these letters:', ' '.join(used_letters))

        #what current word is W - R D
        word_list = [letter if letter in used_letters else '-' for letter in word] #
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters: #if used letter in the alphabet take it out
            used_letters.add(user_letter) #
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1
                print('\nYour letter', user_letter, 'is not in the word')
        
        elif user_letter in used_letters:
            print('\nYou have already used this letter. Try again.')

        else:
            print('\nThat is not a valid letter') # prints for any special characters or numbers

    if lives == 0:
        print('You hvae died the word was', word)
    
    else:
        print('Yay!! you guessed the word', word)

if __name__ == '__main__':
    hangman()

