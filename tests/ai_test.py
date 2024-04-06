import unittest
import time
from src.logic.ai import AI
from src.logic.board import Board

class TestAI(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.manager = StubManager()
        self.ai = AI(2, self.board, self.manager, 6)

    def test_ai_does_not_help_opponent(self):
        self.board.drop(0, 2)
        self.board.drop(0, 2)
        self.board.drop(0, 2)
        self.board.drop(0, 1)
        self.board.drop(0, 2)

        self.board.drop(1, 2)
        self.board.drop(1, 2)
        self.board.drop(1, 2)
        self.board.drop(1, 1)
        self.board.drop(1, 2)

        self.board.drop(2, 1)

        self.board.drop(3, 2)
        self.board.drop(3, 1)
        self.board.drop(3, 1)
        self.board.drop(3, 1)
        self.board.drop(3, 2)

        self.board.drop(4, 1)
        self.board.drop(4, 1)
        self.board.drop(4, 2)
        self.board.drop(4, 1)
        self.board.drop(4, 2)

        self.board.drop(5, 1)
        self.board.drop(5, 2)
        self.board.drop(5, 1)
        self.board.drop(5, 1)
        self.board.drop(5, 2)

        self.board.drop(6, 1)
        self.board.drop(6, 1)
        self.board.drop(6, 1)
        self.board.drop(6, 2)
        self.board.drop(6, 1)

        column = self.ai_choose_column(self.ai)

        self.assertNotEqual(column, 2)
    
    def test_ai_does_not_help_opponent_2(self):
        self.board.drop(0, 2)
        self.board.drop(0, 2)
        self.board.drop(0, 2)
        self.board.drop(0, 1)
        self.board.drop(0, 2)
        self.board.drop(0, 2)

        self.board.drop(1, 2)
        self.board.drop(1, 1)

        self.board.drop(2, 1)
        self.board.drop(2, 2)
        self.board.drop(2, 1)
        self.board.drop(2, 2)

        self.board.drop(3, 1)
        self.board.drop(3, 1)
        self.board.drop(3, 1)
        self.board.drop(3, 2)

        self.board.drop(4, 1)
        self.board.drop(4, 1)
        self.board.drop(4, 2)
        self.board.drop(4, 1)

        self.board.drop(5, 2)
        self.board.drop(5, 1)
        self.board.drop(5, 1)

        column = self.ai_choose_column(self.ai)

        self.assertNotEqual(column, 1)

    # This test was testing a bug that turned out to not be a bug in the AI's current form.
    # The AI knows it is going to lose in the future no matter which move it chooses (assuming the player plays perfectly).
    # This means the AI gave up and chose a random move.
    # This test can however be used in the future once the AI is improved.
    # The AI notices that it is going to lose only if depth >= 6.
    """
    def test_ai_does_not_help_opponent_3(self):
        self.board.drop(0, 2)
        self.board.drop(0, 2)
        self.board.drop(0, 2)
        self.board.drop(0, 1)
        self.board.drop(0, 2)

        self.board.drop(1, 1)

        self.board.drop(2, 1)
        self.board.drop(2, 1)
        self.board.drop(2, 1)
        self.board.drop(2, 2)

        self.board.drop(3, 1)
        self.board.drop(3, 1)
        self.board.drop(3, 1)
        self.board.drop(3, 2)

        self.board.drop(4, 2)
        self.board.drop(4, 2)

        self.board.drop(5, 1)

        ai = AI(2, self.board, self.manager, 6)
        column = self.ai_choose_column(ai)

        self.assertNotEqual(column, 4)
    """

    # Currently it chooses a legal move but a random one.
    def test_ai_chooses_legal_move_when_depth_exceeds_amount_of_open_slots(self):
        for i in range(7):
            for j in range(6):
                if i == 6 and j == 5:
                    break

                player = 0
                if ((i + 1) // 3) % 2 == 0:
                    player = 1
                else:
                    player = 2

                if j % 2 == 1:
                    player = 3 - player

                self.board.drop(i, player)

        column = self.ai_choose_column(self.ai)

        self.assertEqual(column, 6)

    def test_ai_finds_winning_move(self):
        self.board.drop(1, 2)
        self.board.drop(2, 1)
        self.board.drop(2, 2)
        self.board.drop(3, 1)
        self.board.drop(3, 1)
        self.board.drop(3, 2)
        self.board.drop(4, 1)
        self.board.drop(4, 1)
        self.board.drop(4, 1)

        column = self.ai_choose_column(self.ai)

        self.assertEqual(column, 4)

    def test_ai_with_depth_6_finds_guaranteed_win_6_total_moves_into_the_future(self):
        self.board.drop(0, 2)
        self.board.drop(0, 2)
        self.board.drop(0, 2)
        self.board.drop(0, 1)
        self.board.drop(0, 2)

        self.board.drop(1, 1)

        self.board.drop(2, 1)
        self.board.drop(2, 1)
        self.board.drop(2, 1)
        self.board.drop(2, 2)
        self.board.drop(2, 2)

        self.board.drop(3, 1)
        self.board.drop(3, 1)
        self.board.drop(3, 1)
        self.board.drop(3, 2)

        self.board.drop(4, 2)
        self.board.drop(4, 2)

        self.board.drop(5, 1)

        ai = AI(1, self.board, self.manager, 6)
        column = self.ai_choose_column(ai)

        self.assertIn(column, [4, 5])

    def ai_choose_column(self, ai: AI):
        ai.start_turn()

        start_time = time.time()

        while self.manager.end_turn_called_count == 0:
            if time.time() - start_time > 10:
                ai.stop_ai_thread = True
                self.fail("AI did not give a response in 10 seconds")

            time.sleep(0.2)

        return self.manager.end_turn_column_arg

class StubManager:
    def __init__(self) -> None:
        self.end_turn_called_count = 0
        self.end_turn_column_arg = None

    def end_turn(self, column):
        self.end_turn_called_count += 1
        self.end_turn_column_arg = column