from colorama import Fore, Back, Style

class game_state:    
    def __init__(self, max_guesses, puzzle):
        self.max_guesses = max_guesses
        self.guesses = 0
        self.guessed_words = []
        self.puzzle = puzzle
        self.success = False
        self.lost = False
    
    # assumes valid word is identified
    def guess_word(self, word):
        self.guessed_words.append(word)
        if(word == self.puzzle):
            self.success = True
        self.guesses+=1

        if self.guesses >= self.max_guesses:
            self.lost = True
            return -1
        
        return self.max_guesses - self.guesses

class state_printer:
    @staticmethod
    def print_state(state):
        print(f"{Style.BRIGHT}\n==================================={Style.NORMAL}")
        print("Words guessed: {}".format(state.guesses))
        for g in state.guessed_words:
            state_printer.print_word(state, g)
        print("Guesses remaining: {}".format(state.max_guesses - state.guesses))
        print(f"{Style.BRIGHT}==================================={Style.NORMAL}")

    @staticmethod
    def print_word(r, word):
        print_str = ''
        for l in word:
            if(l in r.puzzle):
                if(r.puzzle.index(l) == word.index(l)):
                    print_str += Fore.GREEN + l + Fore.RESET
                else:
                    print_str += Fore.YELLOW + l + Fore.RESET
            else:
                    print_str += Fore.RED + l + Fore.RESET

        print(print_str)