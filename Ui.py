from abc import ABC, abstractmethod
from Game import Game,GameError
from tkinter import Button, Tk, Toplevel, Frame, X

class Ui(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Gui(Ui):
    def __init__(self):
        root = Tk()
        root.title("Tic Tac Toe")
        frame = Frame(root)
        frame.pack()
        
        Button(
            frame,
            text='Show Help',
            command = self._help_callback).pack(fill=X)
        
        Button(
            frame,
            text='Play',
            command = self._play_callback).pack(fill=X)

        Button(
            frame,
            text='Quit',
            command = self._quit_callback).pack(fill=X)
        
        self.__root = root
        
    def _help_callback(self):
        pass
    
    def _play_callback(self):
        pass
        
    def _quit_callback(self):
        self.__root.quit()
    
    def run(self):
        self.__root.mainloop()
        
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
