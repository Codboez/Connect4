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

        self.state = GameState()

    #These tests are outdated since the value amounts have been changed
    """
    def test_calculates_correct_value_when_winning_move_found(self):
        value = self.state.calculate_value_for_player(1, self.board, [5, 6, 5, 6, 0])
        self.assertEqual(value, 10)

    def test_calculates_correct_value_when_winning_move_not_found(self):
        value = self.state.calculate_value_for_player(1, self.board, [3, 4, 6, 6, 6])
        self.assertEqual(value, 5)

    def test_calculates_correct_value_when_winning_move_for_opponent_found(self):
        value = self.state.calculate_value_for_player(1, self.board, [5, 1, 4, 5])
        self.assertEqual(value, 0)
    """