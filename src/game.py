from src.store import build_store
class Game():
    def __init__(self, store, xplayer, oplayer, board):
        self.xplayer = xplayer
        self.oplayer = oplayer
        self.board = board
        self.id = len(store['games']) + 1
        store['games'].append(self)
    def xplayer_moves(self):
        return [[turn.square.index(),['X']] for turn in self.store['turns'] if self.xplayer == turn.user ]
    def oplayer_moves(self):
        return [[turn.square.index(),['O']] for turn in self.store['turns'] if self.oplayer == turn.user ]
    def labeled_moves(self,store):
        labeled_moves = []
        for turn in store['turns']:
            if self.xplayer == turn.user:
                labeled_moves.append([turn.square.index(),['X']])
            if self.oplayer == turn.user:
                labeled_moves.append([turn.square.index(),['O']])
        return labeled_moves
    