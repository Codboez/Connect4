import unittest
from src.logic.game_state import GameState
from src.logic.board import Board

class TestGameState(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.board.drop(0, 1)
        self.board.drop(0, 1)
        self.board.drop(0, 1)
        self.board.drop(1, 2)
        self.board.drop(1, 2)
        self.board.drop(1, 2)
        self.board.drop(0, 1)

        self.state = GameState()

    def test_calculates_correct_value_when_winning_move_found(self):
        value = self.state.calculate_value_for_player(1, self.board, (0, 2))
        self.assertEqual(value, 1006)

    def test_calculates_correct_value_when_winning_move_not_found(self):
        self.board.drop(2, 1)
        value = self.state.calculate_value_for_player(1, self.board, (2, 5))
        self.assertEqual(value, 0)

    def test_calculates_correct_value_when_line_of_three_found(self):
        value = self.state.calculate_value_for_player(2, self.board, (1, 3))
        self.assertEqual(value, 6)