from src.board import Board
from src.game import Game
from src.store import build_store
from src.square import Square
from src.turn import Turn
class Service:
    def __init__(self):
        pass
    def start_game(self, store, xplayer, oplayer):
        board = Board(store)
        return Game(store, xplayer, oplayer, board)

    def take_turn(self, store, game, row, column, user):
        square = Square(game.board, row, column)
        
        if self.validate_turn(square, store):
            Turn(store, user, square)
        else:
            raise Exception('Invalid Move')
        
       
    def validate_turn(self, square, store):
        turn_list = square.board.turns(store)
        if len(turn_list) == 0:
            return True
        for turn in turn_list.values():
            if square.row == turn.square.row and turn.square.col == square.col:
                return False
            else:
                return True
    def prepare_board_state(self, store, game):
        moves = game.labeled_moves(store)
        board_state = {(0, 0): ' ', (0, 1): ' ', (0, 2): ' ', (1, 0): ' ', (1, 1): ' ', (1, 2): ' ', (2, 0): ' ', (2, 1): ' ', (2, 2): ' '}
        for move in moves:
            board_state[move[0]] = move[1][0]
        return board_state
    
    # def order_board_by_index(self, game):
    #     moves = self.prepare_board_state(game)
    #     return sorted(moves, key = lambda x: (x[0][0],x[0][1]))
    def display_board_state(self, board_state):
            print("\n     |     |     ")
            print("  {}  |  {}  |  {}  ".format(board_state[(0,0)], board_state[(0,1)], board_state[(0,2)]))
            print("_____|_____|_____")
            print("     |     |     ")
            print("  {}  |  {}  |  {}  ".format(board_state[(1,0)], board_state[(1,1)], board_state[(1,2)]))
            print("_____|_____|_____")
            print("     |     |     ")
            print("  {}  |  {}  |  {}  ".format(board_state[(2,0)], board_state[(2,1)], board_state[(2,2)]))
            print("     |     |     ")
    def display_custom_board_state(self, rows, columns):
        board_string = ''
        for i in range(rows):
            
            if i < rows-1:
                board_string += '\n'+'     |'*columns + '\n'+'     '+'|  {}  '* columns
                board_string += '\n'+'_____|'*columns
            if i == rows-1:
                board_string += '\n'+ '     |'*columns + '\n'+ '|  {}  ' * columns + '\n'+'     |'* columns
        return board_string
    
    def check_winner(self, board_state):
        full = True
        if ' ' in board_state.values():
            full = False
        index = {index:value for index, value in enumerate(list(board_state.values()), start = 1)}
        check_list = [index[1],index[2],index[3]],[index[4],index[5],index[6]],[index[7],index[8],index[9]],[index[1],index[4],index[7]],[index[2],index[5],index[8]],[index[3],index[6],index[9]],[index[1],index[5],index[9]],[index[3],index[5],index[7]]
        for check in check_list:
            if all(check[0]==x and x!=' ' for x in check):
                print(f"{check[0]} is winner")
                return True
        if full:
            print ("Tie Game")
            return True
        return False
            

        



