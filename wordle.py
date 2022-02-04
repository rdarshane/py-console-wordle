### Developer: Rushikesh Darshane
### NCI MSc Cloud computing
### 03 Feb 2022
### Python based console `wordle` game inspired from online game 
### https://www.powerlanguage.co.uk/wordle/
### create your API key for oxford dictionary for lookup 
### at https://developer.oxforddictionaries.com/ and replace in dictionaryService.py file

from dictionaryService import dictionary_service as ds
from gameState import game_state, state_printer
from puzzle import puzzle 
from dictionaryService import dictionary_service
from help import helper
from colorama import init

init()

helper.get_help()
puzzle_word = puzzle.get_puzzle_word()

state = game_state(6, puzzle_word)

state_printer.print_state(state)

while((state.lost == False) & (state.success ==False)):
    guess = input("Enter your next 5 letter word guess: ")
    if(guess == "??"):
        helper.get_help()
        continue

    if(len(guess) != 5):
        print("Please enter 5 letter word.")
        continue
    
    (valid, dict_entry)= dictionary_service.get_word(guess)
    if(valid):
        state.guess_word(guess)
        if(state.success):
            print("\nYou guessed it right !")
            state_printer.print_state(state)
        else:
            state_printer.print_state(state)
            print("Not a correct guess, try again.")
    else:
        print("Word not found in oxford dictionary!")
    
    if(state.lost):
        print("Sorry, you did not guess word in {} attempts".format(state.max_guesses))
    