
import random
def game_prompt():
    difficulty =input("Welcome to Mystery Words!\n What difficulty level would you like to play on? \n [E]asy   [M]edium   [H]ard ")
    word_list = get_word()
    filtered_word_list = []
    if difficulty == "E":
        for items in word_list:
            if len(items) >= 4 and len(items) <= 6:
                filtered_word_list.append(items)

    if difficulty == "M":
        for items in word_list:
            if len(items) >= 6 and len(items) <= 8:
                filtered_word_list.append(items)

    if difficulty == "H":
        for items in word_list:
            if len(items) >= 8:
                filtered_word_list.append(items)
    return(random.choice(filtered_word_list))         
       
def get_word():
    with open("words.txt") as words_pulled:
        words = words_pulled.readlines()
        return(words)

def format_word():
    word_bank = []
    obtained_word = game_prompt()
    lower_obtained_word = obtained_word.lower()
    all_letters = "abcdefghijklmnopqrstuvwxyz"
    for char in lower_obtained_word:
        if char in all_letters:
            word_bank.append(char)        
    # print(obtained_word)
    # print(word_bank)
    return word_bank

def guess_input():
    guess = input("Guess a Letter!")
    return guess

def display_guesses(letter, guesses):
    if letter in guesses:
        return letter
    else:
        return "_"

def check_guess(letter, word):
    if letter in word:
        return True
    else:
        return False

def play_again():
    answer = input("Would you like to play again? (Y/N) ")
    if answer == "Y" or answer == "y":
        run_game()
    elif answer != "Y" or answer != "y":   
        raise SystemExit
        
def check_valid_guess(guess, current_guesses):
    if guess in current_guesses:
        print("You've already guessed that letter!\n")
        return False
    elif len(guess) > 1:
        print ("One letter at a time, please.\n")
        return False
    elif guess.isalpha() == False:
        print("Your guess wasn't a letter.\n")
        return False
    elif len(guess) == 1 and guess.isalpha() == True and guess not in current_guesses:
        return True

def guess_loop(word, current_guesses, guess_count, output):
    while guess_count !=0:
        letter = guess_input()
        if check_valid_guess(letter, current_guesses) == False:
            guess_loop(word, current_guesses, guess_count,output)
        elif check_valid_guess(letter, current_guesses) == True:
            current_guesses.append(letter)
            check = check_guess(letter, word)
            for letter in word:
                output.append(display_guesses(letter, current_guesses))
            print(output)
            if output == word:
                print("You guessed the word!!")
                play_again()
            output = []
            if check == True:
                print("Letter is in word!")
                print(f"You have {guess_count} guesses remaining\n")

            elif check == False:
                guess_count -= 1
                print("Sorry, guess again!")
                print(f"You have {guess_count} guesses remaining\n") 
    if guess_count == 0:
        print("Sorry, you are out of guesses :(\n")
        print(f"The Mystery Word was {word}")
        play_again()
            
def run_game():
    word = format_word()
    # print(word)
    print(f"Your word is {len(word)} letters long!\n")
    guess_count = 8
    current_guesses = []
    output = []
    guess_loop(word, current_guesses, guess_count,output)            

run_game()

# THIS IS WORKING VALID CODE 
# def run_game():
#     game_prompt()
#     word = format_word()
#     print(word)
#     print(f"Your word is {len(word)} letters long!")
#     guess_count = 8
#     current_guesses = []
#     output = []
#     while guess_count !=0:
#         if output != word:
#             letter = guess_input()
#             if check_valid_guess(letter, current_guesses) == False: letter = guess_input()
#             elif check_valid_guess(letter, current_guesses) == True:
#                 current_guesses.append(letter)
#                 check = check_guess(letter, word)
#                 for letter in word:
#                     output.append(display_guesses(letter, current_guesses))
#                 print(output)
#                 if output == word:
#                     print("You guessed the word!!")
#                     play_again()
#                 output = []
#                 if check == True:
#                     print("Letter is in word!")
#                     print(f"You have {guess_count} guesses remaining")
#                 elif check == False:
#                     guess_count -= 1
#                     print("Sorry, guess again!")
#                     print(f"You have {guess_count} guesses remaining\n") 
#     if guess_count == 0:
#         print("Sorry, you are out of guesses :(\n")
#         play_again()