from src.service import Service
from src.game import Game
from src.square import Square
from src.store import build_store
from src.turn import Turn
from src.board import Board
from src.user import User
import itertools


store = build_store()
service = Service()
player_one = User(store, input('Player1 Name: '))
player_two = User(store, input('Player2 Name: '))
print(service.display_custom_board_state(4,4))
breakpoint()
players = [player_one, player_two]
iterator = itertools.cycle(players)
game = service.start_game(store, player_one, player_two)

while service.check_winner(service.prepare_board_state(store, game)) == False:
    service.take_turn(store, game, int(input('row: ')), int(input('column: ')), next(iterator))
    service.display_board_state(service.prepare_board_state(store, game))




