from src.store import build_store

class Turn:
    def __init__(self, store, user, square):
        self.user = user
        self.square = square
        self.id = len(store['turns']) + 1
        store['turns'].append(self)