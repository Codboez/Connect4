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

        lines = self.board.count_lines_from(4, 3)

        self.assertEqual(lines, [0, 0, 0, 2, 2, 0])

    def test_counts_lines_correctly_2(self):
        self.board.drop(3, 1)
        self.board.drop(2, 2)
        self.board.drop(3, 1)
        self.board.drop(2, 2)
        self.board.drop(3, 1)
        self.board.drop(6, 2)
        self.board.drop(3, 1)

        lines = self.board.count_lines_from(3, 2)

        self.assertEqual(lines, [1, 1, 1, 0, 0, 0])

    def test_counts_lines_correctly_3(self):
        self.board.drop(3, 1)
        self.board.drop(1, 2)
        self.board.drop(3, 1)
        self.board.drop(1, 2)
        self.board.drop(3, 1)
        self.board.drop(6, 2)
        self.board.drop(3, 1)

        lines = self.board.count_lines_from(3, 2)

        self.assertEqual(lines, [1, 1, 1, 0, 0, 0])
