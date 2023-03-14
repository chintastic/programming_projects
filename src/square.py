class Square:
    def __init__(self, board, row, col):
        if row < 0 or row > 2:
            raise Exception("Sorry, improper row index")
        if col < 0 or col > 2:
            raise Exception("Sorry, improper col index")
        self.board = board
        self.row = row
        self.col = col

    def index(self):
        return (self.row, self.col)
