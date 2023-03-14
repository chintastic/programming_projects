from src.store import build_store

class Board:
    def __init__(self, store):
        self.board_id = len(store['boards']) + 1
        store['boards'].append(self)
    def turns(self, store):
        return {turn.id: turn for turn in store['turns'] if self.board_id == turn.square.board.board_id}
    

    
    # def winner(self):
    #     bcount = 0
    #     for r in range(0,3):
    #         xcount1 = 0
    #         xcount2 = 0
    #         ocount1 = 0
    #         ocount2 = 0
    #         for c in range (0,3):
    #             if self.state[r][c] == 'X':
    #                 xcount1 +=1
    #             elif self.state[r][c] == 'O':
    #                 ocount1 +=1
    #             elif self.state[r][c] == '':
    #                 bcunt += 1
    #             if self.state[c][r] == 'X':
    #                 xcount2 +=1
    #             elif self.state[c][r] == 'O':
    #                 ocount2 += 1
    #             elif self.state[c][r] == '':
    #                 bcount += 1
    #         if 3 in (xcount1, xcount2):
    #             return 'X'
    #         if 3 in (ocount1, ocount2):
    #             return 'O'
    #     if bcount > 0:
    #         return 'N/A'
    #     if bcount == 0:
    #         return 'tie'
