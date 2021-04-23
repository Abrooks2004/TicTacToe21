from abc import ABC, abstractmethod
from Game import Game,GameError
from tkinter import Button, Tk, Toplevel, Frame, X, StringVar, Text, Scrollbar, LEFT, RIGHT, Y, END, Grid, N, S, W, E
from itertools import product

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
        
        console = Text(frame, height=4, width=50)
        scroll = Scrollbar(frame)
        scroll.pack(side=RIGHT,fill=Y)
        console.pack(side=LEFT,fill=Y)
        
        scroll.config(command=console.yview)
        console.config(yscrollcommand=scroll.set)
        
        self.__root = root
        self.__console = console
        
    def _help_callback(self):
        with open("HelpDocuments.txt") as f:
            txt = f.read() 
        
        self.__console.insert(END, f"{txt}\n")
    
    def _play_callback(self):
        self.__game = Game()
        game_win = Toplevel(self.__root)
        game_win.title("Game")
        frame = Frame(game_win)

        
        #Resizing
        Grid.columnconfigure(game_win,0,weight=1)
        Grid.rowconfigure(game_win,0,weight=1)
        frame.grid(row=0,column=0,sticky=N+S+W+E)
        
        Button(game_win, text="Dismiss", command=game_win.destroy).grid(row=1,column=0)
        
        self.__buttons = [[None]*3 for _ in range(3)]
        
        for row,col in product(range(3),range(3)):
            b = StringVar()
            b.set(self.__game.at(row+1,col+1))
            
            cmd = lambda r=row, c=col: self.__play_and_refresh(r,c)
            
            Button(frame, textvariable=b, command=cmd).grid(row=row,column=col,sticky=N+S+W+E)
            self.__buttons[row][col] = b
            
        #Resizing
        for i in range(3):    
            Grid.columnconfigure(frame,i,weight=1)
            Grid.rowconfigure(frame,i,weight=1)
            
            
    def __play_and_refresh(self,row,col):
        try:
            self.__game.play(row+1,col+1)
        except GameError as e:
            self.__console.insert(END, f"{e}\n")
            
        for row,col in product(range(3),range(3)):
            text = self.__game.at(row+1,col+1)
            self.__buttons[row][col].set(text)
                
        w = self.__game.winner
        if w is not None:
            if w is Game.DRAW:
                self.__console.insert(END, "The game was drawn\n")
            else:
                self.__console.insert(END, f"The winner was {w}\n")
        
        
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
