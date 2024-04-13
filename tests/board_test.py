import unittest
from src.logic.board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_four_in_line_is_found_horizontally(self):
        self.board.drop(1, 1)
        self.board.drop(0, 2)
        self.board.drop(2, 1)
        self.board.drop(1, 2)
        self.board.drop(3, 1)
        self.board.drop(6, 2)
        self.board.drop(4, 1)

        winning_line = self.board.four_in_line_from(1, 4, 5)

        self.assertEqual(winning_line, ((1, 5), (4, 5)))

    def test_four_in_line_is_found_horizontally_2(self):
        self.board.drop(1, 1)
        self.board.drop(0, 2)
        self.board.drop(2, 1)
        self.board.drop(1, 2)
        self.board.drop(3, 1)
        self.board.drop(6, 2)
        self.board.drop(4, 1)

        winning_line = self.board.four_in_line_from(1, 2, 5)

        self.assertEqual(winning_line, ((1, 5), (4, 5)))

    def test_four_in_line_is_returns_none_when_not_found_horizontally(self):
        self.board.drop(1, 1)
        self.board.drop(0, 2)
        self.board.drop(2, 1)
        self.board.drop(1, 2)
        self.board.drop(3, 1)
        self.board.drop(6, 2)
        self.board.drop(5, 1)

        winning_line = self.board.four_in_line_from(1, 5, 5)

        self.assertEqual(winning_line, None)

    def test_four_in_line_is_returns_none_when_not_found_horizontally_2(self):
        self.board.drop(0, 1)
        self.board.drop(2, 2)
        self.board.drop(1, 1)
        self.board.drop(3, 2)
        self.board.drop(5, 1)
        self.board.drop(4, 2)
        self.board.drop(6, 1)

        winning_line = self.board.four_in_line_from(1, 6, 5)

        self.assertEqual(winning_line, None)

    def test_four_in_line_is_found_vertically(self):
        self.board.drop(1, 1)
        self.board.drop(1, 1)
        self.board.drop(1, 1)
        self.board.drop(1, 1)

        winning_line = self.board.four_in_line_from(1, 1, 2)

        self.assertEqual(winning_line, ((1, 2), (1, 5)))

    def test_four_in_line_is_found_vertically_2(self):
        self.board.drop(4, 2)
        self.board.drop(4, 1)
        self.board.drop(4, 1)
        self.board.drop(4, 1)
        self.board.drop(4, 1)
        self.board.drop(4, 2)

        winning_line = self.board.four_in_line_from(1, 4, 3)

        self.assertEqual(winning_line, ((4, 1), (4, 4)))

    def test_four_in_line_is_returns_none_when_not_found_vertically(self):
        self.board.drop(6, 1)
        self.board.drop(6, 2)
        self.board.drop(6, 2)
        self.board.drop(6, 2)
        self.board.drop(6, 1)
        self.board.drop(6, 2)

        winning_line = self.board.four_in_line_from(2, 6, 1)

        self.assertEqual(winning_line, None)

    def test_four_in_line_is_returns_none_when_not_found_vertically_2(self):
        self.board.drop(0, 1)
        self.board.drop(0, 1)
        self.board.drop(0, 2)
        self.board.drop(0, 2)
        self.board.drop(0, 1)
        self.board.drop(0, 1)

        winning_line = self.board.four_in_line_from(1, 0, 0)

        self.assertEqual(winning_line, None)

    def test_four_in_line_is_found_diagonally(self):
        self.board.drop(1, 1)
        self.board.drop(2, 2)
        self.board.drop(2, 1)
        self.board.drop(3, 2)
        self.board.drop(3, 2)
        self.board.drop(3, 1)
        self.board.drop(4, 2)
        self.board.drop(4, 2)
        self.board.drop(4, 2)
        self.board.drop(4, 1)

        winning_line = self.board.four_in_line_from(1, 4, 2)

        self.assertEqual(winning_line, ((1, 5), (4, 2)))

    def test_four_in_line_is_found_diagonally_2(self):
        self.board.drop(0, 2)
        self.board.drop(0, 1)
        self.board.drop(1, 2)
        self.board.drop(1, 2)
        self.board.drop(1, 1)
        self.board.drop(2, 2)
        self.board.drop(2, 2)
        self.board.drop(2, 2)
        self.board.drop(2, 1)
        self.board.drop(3, 1)
        self.board.drop(3, 2)
        self.board.drop(3, 2)
        self.board.drop(3, 2)
        self.board.drop(3, 1)

        winning_line = self.board.four_in_line_from(1, 1, 3)

        self.assertEqual(winning_line, ((0, 4), (3, 1)))

    def test_four_in_line_is_found_diagonally_3(self):
        self.board.drop(6, 1)
        self.board.drop(5, 2)
        self.board.drop(5, 1)
        self.board.drop(4, 2)
        self.board.drop(4, 2)
        self.board.drop(4, 1)
        self.board.drop(3, 2)
        self.board.drop(3, 2)
        self.board.drop(3, 2)
        self.board.drop(3, 1)

        winning_line = self.board.four_in_line_from(1, 3, 2)

        self.assertEqual(winning_line, ((3, 2), (6, 5)))

    def test_four_in_line_is_found_diagonally_4(self):
        self.board.drop(4, 2)
        self.board.drop(4, 1)
        self.board.drop(3, 2)
        self.board.drop(3, 2)
        self.board.drop(3, 1)
        self.board.drop(2, 2)
        self.board.drop(2, 2)
        self.board.drop(2, 2)
        self.board.drop(2, 1)
        self.board.drop(1, 1)
        self.board.drop(1, 2)
        self.board.drop(1, 2)
        self.board.drop(1, 2)
        self.board.drop(1, 1)

        winning_line = self.board.four_in_line_from(1, 3, 3)

        self.assertEqual(winning_line, ((1, 1), (4, 4)))

    def test_four_in_line_is_returns_none_when_not_found_diagonally(self):
        self.board.drop(1, 1)
        self.board.drop(2, 2)
        self.board.drop(2, 2)
        self.board.drop(3, 2)
        self.board.drop(3, 2)
        self.board.drop(3, 1)
        self.board.drop(4, 2)
        self.board.drop(4, 2)
        self.board.drop(4, 2)
        self.board.drop(4, 1)

        winning_line = self.board.four_in_line_from(1, 3, 3)

        self.assertEqual(winning_line, None)

    def test_four_in_line_is_returns_none_when_not_found_diagonally_2(self):
        self.board.drop(3, 1)
        self.board.drop(3, 1)
        self.board.drop(3, 1)
        self.board.drop(3, 2)
        self.board.drop(3, 2)
        self.board.drop(4, 2)
        self.board.drop(4, 1)
        self.board.drop(4, 2)
        self.board.drop(4, 1)
        self.board.drop(4, 1)
        self.board.drop(4, 2)
        self.board.drop(5, 2)
        self.board.drop(6, 1)
        self.board.drop(6, 2)

        winning_line = self.board.four_in_line_from(2, 4, 0)

        self.assertEqual(winning_line, None)

    def test_four_in_line_is_returns_none_when_not_found_diagonally_3(self):
        self.board.drop(6, 2)
        self.board.drop(5, 2)
        self.board.drop(5, 1)
        self.board.drop(4, 2)
        self.board.drop(4, 2)
        self.board.drop(4, 1)
        self.board.drop(3, 2)
        self.board.drop(3, 2)
        self.board.drop(3, 2)
        self.board.drop(3, 1)

        winning_line = self.board.four_in_line_from(1, 3, 2)

        self.assertEqual(winning_line, None)

    def test_four_in_line_is_returns_none_when_not_found_diagonally_4(self):
        self.board.drop(3, 1)
        self.board.drop(3, 1)
        self.board.drop(3, 1)
        self.board.drop(3, 2)
        self.board.drop(3, 2)
        self.board.drop(2, 2)
        self.board.drop(2, 1)
        self.board.drop(2, 2)
        self.board.drop(2, 1)
        self.board.drop(2, 1)
        self.board.drop(2, 2)
        self.board.drop(1, 2)
        self.board.drop(0, 1)
        self.board.drop(0, 2)

        winning_line = self.board.four_in_line_from(2, 0, 4)

        self.assertEqual(winning_line, None)

    def test_counts_lines_correctly(self):
        self.board.drop(1, 1)
        self.board.drop(2, 2)
        self.board.drop(2, 1)
        self.board.drop(3, 2)
        self.board.drop(3, 2)
        self.board.drop(3, 1)
        self.board.drop(4, 2)
        self.board.drop(4, 2)
        self.board.drop(4, 2)

        lines = self.board.count_lines_from(4, 3, 2)

        self.assertEqual(lines, [2, 2, 0])

    def test_counts_lines_correctly_2(self):
        self.board.drop(3, 1)
        self.board.drop(2, 2)
        self.board.drop(3, 1)
        self.board.drop(2, 2)
        self.board.drop(3, 1)
        self.board.drop(6, 2)
        self.board.drop(3, 1)

        lines = self.board.count_lines_from(3, 2, 1)

        self.assertEqual(lines, [1, 1, 1])

    def test_counts_lines_correctly_3(self):
        self.board.drop(3, 1)
        self.board.drop(1, 2)
        self.board.drop(3, 1)
        self.board.drop(1, 2)
        self.board.drop(3, 1)
        self.board.drop(6, 2)
        self.board.drop(3, 1)

        lines = self.board.count_lines_from(3, 2, 1)

        self.assertEqual(lines, [1, 1, 1])

    def test_drop_drops_a_coin_to_the_correct_height(self):
        self.board.set_slot(3, 5, 2)
        self.board.set_slot(3, 4, 2)

        self.board.drop(3, 1)

        self.assertEqual(self.board.get_slot(3, 3), 1)

    def test_drop_raises_value_error_when_column_is_full(self):
        for _ in range(6):
            self.board.drop(2, 1)

        self.assertRaises(ValueError, self.board.drop, 2, 1)

    def test_gets_legal_moves_correctly(self):
        for i in range(0, 7, 2):
            for _ in range(6):
                self.board.drop(i, 1)

        legal_moves = self.board.get_legal_moves()

        self.assertListEqual(legal_moves, [1, 3, 5])

    def test_board_copies_itself_correctly(self):
        self.board.drop(1, 2)
        self.board.drop(2, 1)
        self.board.drop(2, 2)

        copy = self.board.copy()

        for y in range(6):
            for x in range(7):
                self.assertEqual(copy.get_slot(x, y), self.board.get_slot(x, y))

    def test_modifying_copied_board_does_not_modify_original(self):
        self.board.drop(1, 2)

        copy = self.board.copy()
        copy.drop(1, 1)

        self.assertEqual(self.board.get_slot(1, 4), 0)

    def test_check_win_finds_winning_line(self):
        self.board.drop(1, 1)
        self.board.drop(2, 1)
        self.board.drop(3, 1)
        self.board.drop(4, 1)

        winning_line = self.board.check_win(1)

        self.assertEqual(winning_line, ((1, 5), (4, 5)))