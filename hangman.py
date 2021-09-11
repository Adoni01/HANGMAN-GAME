
import random
from words import words 
import string

def get_valid_word(words):
    word = random.choice(words)  # choose randomly in the list 
    while '_' in word or '' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  #letter in the word 
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # to store  what the user guessed

    lives = 7
    
    #getting user input 
    while len(word_letters) > 0 and lives > 0 :
        #letters used 
        # ' '. join(['a','b','cd'])--->'a b cd '
        print('you have ',lives,'lives left and you have used these letters :',' '.join(used_letters))

        #which is the current word 
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('current word:',' '.join(word_list))



        user_letter = input('guess a letter :').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                lives = lives - 1 # takes a life 
                print('letter not in a word ')
        elif user_letter in used_letters:
            print("you gueessed that already")
        else:
            print("you typed an invalid character try again")
    
    #gets here when the len(word_letters) ==0 or when lives  == 0
    if lives == 0 :
        print('you died and the word is ',word)
    else:

        print ('you guessed the word ',word,'!!!!!' )  




if __name__ == '__main__':
    hangman()