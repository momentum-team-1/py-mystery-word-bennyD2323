program start

ask for Easy, Med, Hard Difficulty
return Value
    if Easy, select short word
    if Med, select Med word
    if Hard, select long word

Set Guesses to 8

pass along word, transform it into List or W.E
create guess list, or comparison list, whatever, some other list for guessing

Prompt input for Guessed Letter

    compare Guessed letter to contents of word list
    if letter is contained in the list, take its Index position
    update the index of the comparison list with the value of the Letter

    if letter is NOT in list, Remove a guess counter from Guesses#
    say WRONGGGGGG
    prompt for more Guesses

if Guesses# is 0 or w.e it runs out
    End game. "Sorry, you lose"
    want to play again?
    yes = loop
    no = quit

If Word List ==== comparison list 
    you win!
    want to play again?
    yes = loop 
    no = quit