import unittest
import hypothesis.strategies as strategies
from hypothesis import given, settings
import timeit
import time
from src.logic.ai import AI
from src.logic.board import Board

class TestAI(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.manager = StubManager()
        self.visualizer = StubVisualizer()
        self.ai = AI(2, self.board, self.manager, 3, self.visualizer, use_iterative_deepening=False)

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

        ai = AI(2, self.board, self.manager, 6, self.visualizer)
        column = self.ai_choose_column(ai)

        self.assertNotEqual(column, 4)

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

        ai = AI(1, self.board, self.manager, 6, self.visualizer)
        column = self.ai_choose_column(ai)

        self.assertIn(column, [4, 5])

    @given(moves=strategies.lists(strategies.integers(min_value=0, max_value=6), min_size=0, max_size=30))
    @settings(max_examples=20, deadline=None)
    def test_alpha_beta_pruning_makes_minimax_faster(self, moves):
        board = Board()
        counts = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
        for i in range(len(moves)):
            if counts[moves[i]] < 6:
                board.drop(moves[i], (i % 2) + 1)
                counts[moves[i]] += 1

        board_copy = board.copy()
        ai_no_pruning = AI(2, board, self.manager, 3, self.visualizer, False, False)
        ai_with_pruning = AI(2, board_copy, self.manager, 3, self.visualizer, True, False)

        no_pruning_time = timeit.timeit(lambda: ai_no_pruning.start_turn(False), number=5)
        with_pruning_time = timeit.timeit(lambda: ai_with_pruning.start_turn(False), number=5)

        self.assertGreaterEqual(no_pruning_time, with_pruning_time)

    def test_alpha_beta_pruning_with_high_depth_makes_minimax_much_faster(self):
        board_copy = self.board.copy()
        ai_no_pruning = AI(2, self.board, self.manager, 5, self.visualizer, False, False)
        ai_with_pruning = AI(2, board_copy, self.manager, 5, self.visualizer, True, False)

        no_pruning_time = timeit.timeit(lambda: ai_no_pruning.start_turn(False), number=3)
        with_pruning_time = timeit.timeit(lambda: ai_with_pruning.start_turn(False), number=3)

        self.assertGreaterEqual(no_pruning_time / 10, with_pruning_time)

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

class StubVisualizer:
    def add_node(self, a, b):
        pass

    def add_value(self, a, b, c):
        pass

    def set_enabled(self, a):
        pass