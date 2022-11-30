import abc


class AbstractPlayer(abc.ABC):
    def __int__(self):
        pass
    
    @abc.abstractmethod
    def ask_card(self):
        pass

    
class Player(AbstractPlayer):
    pass


class Dealer(AbstractPlayer):
    pass


class Bot(AbstractPlayer):
    pass
