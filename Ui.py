from abc import ABC, abstractmethod
from Game import Game,GameError

class Ui(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Gui(Ui):
    def __init__(self):
        pass

    def run(self):
        print("Running GUI")

class Terminal(Ui):
    def __init__(self):
        self.__game = Game()

    def run(self):
        while not self.__game.winner:
            print(self.__game)
            try:
                row = int(input("Enter the row: "))
                col = int(input("Enter the column"))
            except TypeError:
                print("Non numeric input")
                continue
                
            if 1 <= row <= 3 and 1<= col <= 3:
                try:
                    self.__game.play(row,col)
                except GameError:
                    print("Invalid Location")
            else:print("Row and column must be between the values of 1 and 3")
        
        if self.__game.winner == Game.DRAW:
            print("The game was drawn")
        else:
            print(self.__game)
            w = self.__game.winner
            print(f"The winner was {w}")
