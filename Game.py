from itertools import product

class GameError(Exception):
    pass

class Game:
    EMPTY = " "
    P1 = "o"
    P2 = "x"
    _DIM = 3
    DRAW = "neither"
    
    def __init__(self):
        self.__board = [[Game.EMPTY]*3 for _ in range(3)]
        self.__player = Game.P1
        
    def __repr__(self):
        result = "  " + " ".join(str(i+1) for i in range(Game._DIM))
        for row in range(Game._DIM):
            result += f"\n{row+1} " + "|".join(self.__board[row])
            if row != Game._DIM - 1:
                dashes = "-" * (2 * Game._DIM - 1)
                result += f"\n  {dashes}"
        result += f"\n\n{self.__player} turn to play"
        return result


    def play(self,row,col):
        row -= 1
        col -= 1
        if self.__board[row][col] != Game.EMPTY:
            raise GameError
        
        self.__board[row][col] = self.__player    
        self.__player = Game.P2 if self.__player is Game.P1 else Game.P1

    
    @property
    def winner(self):
        for p in [Game.P1,Game.P2]:
            for row in range(Game._DIM):
                if all(self.__board[row][col] is p for col in range(Game._DIM)):
                    return p
            for col in range(Game._DIM):
                if all(self.__board[row][col] is p for row in range(Game._DIM)):
                    return p
            if all(self.__board[i][i] is p for i in range(Game._DIM)):
                return p
            if all(self.__board[i][Game._DIM - 1 - i] is p for i in range(Game._DIM)):
                return p
        numempty = 0
        for r,c in product(range(3),range(3)):
            if self.__board[r][c] == Game.EMPTY:
                numempty += 1
        if numempty == 0:
            return Game.DRAW
        return None

if __name__ == "__main__":
    g = Game()
    print(g)
