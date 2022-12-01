from Player import Bot
from const import MESSAGES
from Deck import Deck

import random


class Game:
    
    def __init__(self):
        self.players = []
        self.player = None
        self.dealer = None
        self.all_players_count = 1
        self.deck = Deck()
        
    
    @staticmethod
    def _ask_starting(message):
        while True:
            choise = input(message)
            if choise == "n":
                return False
            elif choise == "y":
                return True
    
    def start_game(self):
        message = MESSAGES.get("ask_start")
        if not self._ask_starting(message=message):
            exit(1)
        
        bots_count = int(input("hello, write bots number "))
        self.all_players_count = bots_count + 1
        for _ in range(bots_count):
            b = Bot(position=random.randint(0, self.all_players_count))
            
            self.players.append(b)
