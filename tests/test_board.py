from src.board import Board
from src.square import Square
from src.store import build_store
from src.user import User
from src.turn import Turn
from src.game import Game
from src.service import Service

def test_init_squares():
    store = build_store()
    board = Board(store)
    square = Square(board,1,2)
    assert square.board == board
    assert square.row == 1
    assert square.col == 2

def test_init_boards():
    store = build_store()
    board1 = Board(store)
    board2 = Board(store)
    assert board1.board_id == 1
    assert board2.board_id == 2

def test_init_users():
    store = build_store()
    user1 = User(store, 'Bob')
    user2 = User(store, 'Chinmay')
    assert user1.name == 'Bob'
    assert user1.id == 1
    assert user2.id == 2

def test_init_turns():
    store = build_store()
    board = Board(store)
    user1 = User(store, 'Bob')
    user2 = User(store, 'Chinmay')
    square1 = Square(board, 1, 2)
    square2 = Square(board, 2, 1)
    turn1 = Turn(store, user1, square1)
    turn2 = Turn(store, user2, square2)
    assert turn1.id == 1
    assert turn2.id == 2
    assert turn2.square == square2
    assert turn2.user == user2

def test_board_turns():
    store = build_store()
    board = Board(store)
    user1 = User(store, 'Bob')
    user2 = User(store, 'Chinmay')
    game = Game(store, user1, user2, board)
    square1 = Square(board, 1, 2)
    square2 = Square(board, 2, 1)
    turn1 = Turn(store, user1, square1)
    turn2 = Turn(store, user2, square2)
    assert board.turns() == {1:turn1, 2:turn2}

def test_service_make_turn():
    store = build_store()
    service = Service()
    board = Board(store)
    user1 = User(store, 'Bob')
    user2 = User(store, 'Chinmay')
    game = Game(store, user1, user2, board)
    square1 = Square(board, 1, 2)
    square2 = Square(board, 2, 1)
    square3 = Square(board, 0, 2)
    turn1 = Turn(store, user1, square1)
    turn2 = Turn(store, user2, square2)
    turn3 = Turn(store, user1, square3)
    service.display_board_state(service.prepare_board_state(game))

def test_service_make_turn_winner():
    store = build_store()
    service = Service()
    board = Board(store)
    user1 = User(store, 'Bob')
    user2 = User(store, 'Chinmay')
    game = Game(store, user1, user2, board)
    square1 = Square(board, 1, 2)
    square2 = Square(board, 2, 1)
    square3 = Square(board, 0, 2)
    square4 = Square(board, 1, 1)
    square5 = Square(board, 2, 2)

    turn1 = Turn(store, user1, square1)
    turn2 = Turn(store, user2, square2)
    turn3 = Turn(store, user1, square3)
    turn4 = Turn(store, user2, square4)
    turn5 = Turn(store, user1, square5)
    service.display_board_state(service.prepare_board_state(game))

def test_service_make_turn_tie():
    store = build_store()
    service = Service()
    board = Board(store)
    user1 = User(store, 'Bob')
    user2 = User(store, 'Chinmay')
    game = Game(store, user1, user2, board)
    square1 = Square(board, 1, 1)
    square2 = Square(board, 2, 0)
    square3 = Square(board, 1, 0)
    square4 = Square(board, 1, 2)
    square5 = Square(board, 0, 1)
    square6 = Square(board, 2, 1)
    square7 = Square(board, 0, 0)
    square8 = Square(board, 2, 2)
    square9 = Square(board, 0, 2)

    turn1 = Turn(store, user1, square1)
    turn2 = Turn(store, user2, square2)
    turn3 = Turn(store, user1, square3)
    turn4 = Turn(store, user2, square4)
    turn5 = Turn(store, user1, square5)
    turn6 = Turn(store, user2, square6)
    turn7 = Turn(store, user1, square7)
    turn8 = Turn(store, user2, square8)
    turn9 = Turn(store, user1, square9)
    service.display_board_state(service.prepare_board_state(game))

