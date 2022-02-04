from colorama import Fore, Back, Style

class helper:
    @staticmethod
    def get_help():
        
        print(f"{Style.BRIGHT}########################################{Style.NORMAL}")
        print("Enter `??` to print this help again... How to play ?")
        print("Guess 5 letter word, you get 6 attempts")
        print("Every guess will tell you")
        print("\n1. if your guess of whole word is right")
        print(f"2. if letters are in right {Fore.GREEN}p{Fore.RESET}lace ")
        print(f"3. if letters are {Fore.YELLOW}rp{Fore.RESET}esent (read as present), but in wrong place")
        print(f"4. if letters are not {Fore.RED}ab{Fore.RESET} (read as present) in the word")
        print("\nUses oxford dictionary API for word lookup. Get your free credentials, link given below. Replace in dictionaryService.py ")
        print("https://developer.oxforddictionaries.com/")

        print(f"{Style.BRIGHT}########################################{Style.NORMAL}")

