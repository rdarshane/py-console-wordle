import random
import json
from datetime import datetime


class puzzle:
    @staticmethod
    def get_puzzle_word ():
    
        with open('words.json') as json_file:
            words = json.load(json_file)

        random.seed(10)

        counter = 0
        parsed_words= []
        for word in words :
            parsed_words.append(word)
            counter+=1

        now = datetime.now()
        rr = now.minute * now.second * now.hour

        index = int(random.random() * 1000 * rr)

        while index > counter:
            index = index// counter

        puzzle_word = parsed_words[index]
        return puzzle_word