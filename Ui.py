from abc import ABC, abstractmethod

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
            row = int(input("Enter the row: "))
            col = int(input("Enter the column"))
            self.__game.play(row,col)
        
