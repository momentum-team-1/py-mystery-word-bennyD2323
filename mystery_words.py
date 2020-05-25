
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
    guess = input("Guess a Letter!")
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


# CHANGE TO INPUT
def game_prompt():
    print("Welcome to Mystery Words!\n What difficulty level would you like to play on? \n [E]asy   [M]edium   [Hard] ")
    

def play_again():
    answer = input("Would you like to play again? (Y/N) ")
    if answer == "Y" or answer == "y":
        run_game()
    elif answer != "Y" or answer != "y":   
        raise SystemExit
        




def check_valid_guess(guess, current_guesses):
    if guess in current_guesses:
        print("You've already guessed that letter!\nGuess again")
        return False
    elif len(guess) > 1:
        print ("One letter at a time, please.\nGuess again")
        return False
    elif guess.isalpha() == False:
        print("Your guess wasn't a letter.\nGuess again")
        return False
    elif len(guess) == 1 and guess.isalpha() == True and not guess in current_guesses:
        print("it works benny")
        return True









def run_game():
    game_prompt()
    word = format_word()
    print(word)
    print(f"Your word is {len(word)} letters long!")
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
                play_again()
            output = []
            if check == True:
                print("Letter is in word!")
                print(f"You have {guess_count} guesses remaining")

            elif check == False:
                guess_count -= 1
                print("Sorry, guess again!")
                print(f"You have {guess_count} guesses remaining\n") 
    if guess_count == 0:
        print("Sorry, you are out of guesses :(\n")
        play_again()




run_game()
