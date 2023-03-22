from copy import deepcopy

class Board():
    def __init__(self):
        self.board = [[" ", "x", "x"],
                      [" ", "x", "o"],
                      ["o", "o", " "]]
        self.backup = self.board.copy()
        self.turn = "x"
        self.winner = None

    def CheckTerminal(self):
        if all([all([pos != ' ' for pos in i]) for i in self.backup]):
            return True
        return False

    def __repr__(self) -> str:
        return f"""
{self.turn}:\n{self.PrintBoard()}"""

    def PrintBoard(self):
        ans = ''
        for line in self.backup:
            ans += f'{line}\n'
        return ans

    def Utility(self):
        self.board = [[1 if pos == 'x' else -1 if pos == 'o' else 0 for pos in i] for i in self.backup]
        length = len(self.board)
        for line in self.board:
            lsum = sum(line)
            if abs(lsum) == length:
                return int(lsum / length)
        lsum = sum([self.board[i][i] for i in range(length)])
        if abs(lsum) == length:
            return int(lsum / length)
        lsum = sum([self.board[length - 1 - i][i] for i in range(length - 1, -1, -1)])
        if abs(lsum) == length:
            return int(lsum / length)
        for pos in range(length):
            lsum = sum([self.board[i][pos] for i in range(length)])
            if abs(lsum) == length:
                return int(lsum / length)
        if self.CheckTerminal():
            return 0
        return False

    def PossibleMoves(self):
        total = 0
        for y, line in enumerate(self.backup):
            for x, pos in enumerate(line):
                nextBoard = deepcopy(self)
                if pos == ' ':
                    total += 1
                    nextBoard.backup[y][x] = self.turn
                    nextBoard.turn = 'o' if self.turn == 'x' else 'x'
                    yield nextBoard
        if total == 0:
            return self.Utility()

    def MaxValue(self):
        result = self.Utility()
        if result is not False:
            return result
        v = -1000
        for pos in a.PossibleMoves():
            ###here do more correctly
            v = max(v, pos.MinValue())
        return v


    def MinValue(self):
        result = self.Utility()
        if result is not False:
            return result
        v = 1000
        for pos in a.PossibleMoves():
            ###here do more correctly
            v = min(v, pos.MaxValue())
        return v

if __name__ == '__main__':
    a = Board()
    print(a.MaxValue())
    
        