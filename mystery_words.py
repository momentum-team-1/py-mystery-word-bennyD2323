
import random

def get_word():
    with open("words.txt") as words_pulled:
        words = words_pulled.readlines()
        return(random.choice(words))

def format_word():
    word_bank = []
    obtained_word = get_word()
    lower_obtained_word = obtained_word.lower()
    all_letters = "abcdefghijklmnopqrstuvwxyz"
    for char in lower_obtained_word:
        if char in all_letters:
            word_bank.append(char)        
    print(obtained_word)
    print(word_bank)
    return word_bank

def guess_input():
    guess = input("Guess a Letter! ")
    return guess
def display_right_guesses(letter, guesses):
    if letter in guesses:
        return letter
    else:
        return "_"

def check_guess(letter, word):
    if letter in word:
        return True
    else:
        return False

    # THIS IS THE WORKING RUN GAME FUNCTION
# def run_game():
#     word = format_word()
#     print(word)
#     guess_count = 0
#     current_guesses = []
#     output = []
#     letter = guess_input()
#     current_guesses.append(letter)
#     check = check_guess(letter, word)
#     for letter in word:
#         output.append(display_right_guesses(letter, current_guesses))
#     if check == True:
#         print("Letter is in word!")
#     else:
#             print("Sorry, guess again!")
#             guess_count += 1
#     print(current_guesses)
#     print(output)

def run_game():
    word = format_word()
    print(word)
    guess_count = 8
    current_guesses = []
    output = []


    while guess_count !=0:
        if output != word:
            letter = guess_input()
            current_guesses.append(letter)
            check = check_guess(letter, word)
            for letter in word:
                output.append(display_right_guesses(letter, current_guesses))
            print(output)
            if output == word:
                print("You guessed the word!!")
                answer = input("Would you like to play again? (Y/N) ")
                if answer == "Y":
                    run_game()
                else:    
                    raise SystemExit
            output = []
            if check == True:
                print("Letter is in word!")

            elif check == False:
                guess_count -= 1
                print("Sorry, guess again!")
                print(f"You have {guess_count} guesses remaining") 

run_game()
