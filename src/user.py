from src.store import build_store
class User():
    def __init__(self, store, name):
        self.id = len(store['users']) + 1
        self.name = name
        store['users'].append(self)
