# access words.txt 
#  randomly select a word

#  display as empty spaces,

#  tell user how many letters
#     if wrong -remove a possible guess (from 8)
#         if # of guesses = 0, player loses the game
# if correct, fill in letter
# guess a letter
# choose difficulty level

import random
def get_word():
    with open("words.txt") as words_pulled:
        words = words_pulled.readlines()
        return(random.choice(words))
# print(get_word())

def format_word():
    word_bank = []
    working_word_bank = []
    obtained_word = get_word()
    all_letters = "abcdefghijklmnopqrstuvwxyz"
    for char in obtained_word:
        
        if char in all_letters:
            word_bank.append(char)
            working_word_bank.append("_")
    print(obtained_word)
    print(word_bank)
    print(word_bank[2])
    print(working_word_bank)
    return word_bank


def guess_input():
    a = format_word()
    
    guess = input("Guess a Letter!")
    print(guess)
    for letter in a:
        if letter == guess:
            return True 

guess_input()
    

