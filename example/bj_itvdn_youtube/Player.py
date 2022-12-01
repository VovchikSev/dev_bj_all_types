import abc
from Deck import Deck


class AbstractPlayer(abc.ABC):
    def __int__(self, position):
        self.cards = []
        self.position = position
    
    def ask_card(self, deck):
        card = deck.get_card()
        self.cards.append(card)
        return True


class Player(AbstractPlayer):
    pass


class Dealer(AbstractPlayer):
    pass


class Bot(AbstractPlayer):
    pass
