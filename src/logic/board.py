import re

class Board:
    def __init__(self) -> None:
        self.__board_list = []
        for _ in range(6):
            self.__board_list.append([0]*7)

    def get_slot(self, x, y):
        return self.__board_list[y][x]

    def set_slot(self, x, y, controller_number):
        self.__board_list[y][x] = controller_number

    def drop(self, x, controller_number):
        """Drops a coin in to the column of the given x index, and places
        it in the closest available slot to the bottom.

        Args:
            x (int): x index of the column to drop the coin in
            controller_number (int): Which player's coin to drop. 1 for player 1. 2 for player 2.

        Raises:
            ValueError: Raised when the x index was out of range.
            ValueError: Raised when the given column is full.

        Returns:
            tuple: The indices of the location the coin was placed into.
        """

        if x >= len(self.__board_list[0]) or x < 0:
            raise ValueError("x index was out of range")

        for i in range(-1, -len(self.__board_list) - 1, -1):
            if self.get_slot(x, i) == 0:
                self.set_slot(x, i, controller_number)
                return (x, len(self.__board_list) + i)

        raise ValueError("Column is full")

    def check_win(self, player):
        """Checks if the given player has won.

        Args:
            player (int): Which player to check the win for. 1 for player 1. 2 for player 2.

        Returns:
            tuple: Contains 2 tuples. The winning line's start and end positions.
            Returns None if given player has not won.
        """

        for y in range(len(self.__board_list)):
            for x in range(len(self.__board_list[y])):
                line = self.four_in_line_from(player, x, y)

                if line is not None:
                    return line

        return None

    def four_in_line_from(self, player, x_index, y_index):
        """Checks if given player has connected four in any direction starting from the given indices.

        Args:
            player (int): Which player to check the win for. 1 for player 1. 2 for player 2.
            x_index (int): x index of the checked position.
            y_index (int): y index of the checked position.

        Returns:
            tuple: Contains 2 tuples. The winning line's start and end positions.
            Returns None if four in line not found.
        """

        line = self.__four_in_line_horizontal(player, y_index)
        if line is not None:
            return line

        line = self.__four_in_line_vertical(player, x_index)
        if line is not None:
            return line

        line = self.__four_in_line_diagonal_1(player, x_index, y_index)
        if line is not None:
            return line

        line = self.__four_in_line_diagonal_2(player, x_index, y_index)
        if line is not None:
            return line

        return None

    def copy(self):
        """Makes a copy of this board.

        Returns:
            Board: The new copy of this board.
        """
        copy_board = Board()

        copy_list = []
        for row in self.__board_list:
            copy_list.append(row.copy())

        copy_board.__board_list = copy_list # pylint: disable=protected-access,unused-private-member
        return copy_board

    def __repr__(self):
        return self.__board_list.__repr__()

    def __four_in_line_horizontal(self, player, y_index):
        """Checks if the given player has a line of four horizontally in the row of the given y index.

        Args:
            player (int): Which player to check the line of four for. 1 for player 1. 2 for player 2.
            y_index (int): The index of the row where to check for the line of four.

        Returns:
            tuple: Contains 2 tuples. The winning line's start and end positions.
            Returns None if four in line not found.
        """
        row = self.__board_list[y_index]
        indices = self.__list_contains_4(row, player)

        if indices is None:
            return None

        return ((indices[0], y_index), (indices[1], y_index))

    def __four_in_line_vertical(self, player, x_index):
        """Checks if the given player has a line of four vertically in the column of the given x index.

        Args:
            player (int): Which player to check the line of four for. 1 for player 1. 2 for player 2.
            x_index (int): The index of the column where to check for the line of four.

        Returns:
            tuple: Contains 2 tuples. The winning line's start and end positions.
            Returns None if four in line not found.
        """
        column = self.__get_vertical_list(x_index)

        indices = self.__list_contains_4(column, player)

        if indices is None:
            return None

        return ((x_index, indices[0]), (x_index, indices[1]))

    def __four_in_line_diagonal_1(self, player, x_index, y_index):
        """Checks if the given player has a line of four diagonally from the
        top left to the bottom right starting from the given indices.

        Args:
            player (int): Which player to check the line of four for. 1 for player 1. 2 for player 2.
            x_index (int): The x index of the position where to check for the line of four.
            y_index (int): The y index of the position where to check for the line of four.

        Returns:
            tuple: Contains 2 tuples. The winning line's start and end positions.
            Returns None if four in line not found.
        """
        i = min(x_index, y_index)

        diagonal_list = self.__get_diagonal_1_list(x_index, y_index)

        indices = self.__list_contains_4(diagonal_list, player)

        if indices is None:
            return None

        line_start = (x_index - i + indices[0], y_index - i + indices[0])
        line_end = (x_index - i + indices[1], y_index - i + indices[1])
        return (line_start, line_end)

    def __four_in_line_diagonal_2(self, player, x_index, y_index):
        """Checks if the given player has a line of four diagonally from the
        bottom left to the top right starting from the given indices.

        Args:
            player (int): Which player to check the line of four for. 1 for player 1. 2 for player 2.
            x_index (int): The x index of the position where to check for the line of four.
            y_index (int): The y index of the position where to check for the line of four.

        Returns:
            tuple: Contains 2 tuples. The winning line's start and end positions.
            Returns None if four in line not found.
        """
        i = 0
        while x_index - i > 0 and y_index + i < 5:
            i += 1

        diagonal_list = self.__get_diagonal_2_list(x_index, y_index)

        indices = self.__list_contains_4(diagonal_list, player)

        if indices is None:
            return None

        line_start = (x_index - i + indices[0], y_index + i - indices[0])
        line_end = (x_index - i + indices[1], y_index + i - indices[1])
        return (line_start, line_end)

    def __get_vertical_list(self, x_index):
        """Get a list of all vertical slots in the given x index.

        Args:
            x_index (int): The index of the column.

        Returns:
            list: The list of all vertical slots in the given x index.
        """
        column = []
        for row in self.__board_list:
            column.append(row[x_index])

        return column

    def __get_diagonal_1_list(self, x_index, y_index):
        """Get a list of all slots found diagonally from the given indices in the top left to bottom right direction.

        Args:
            x_index (int): The x index of the position where to get the diagonal list from.
            y_index (int): The y index of the position where to get the diagonal list from.

        Returns:
            list: List of all diagonal slots from the given indices.
        """
        i = min(x_index, y_index)

        diagonal_list = []
        j = 0
        while x_index - i + j < 7 and y_index - i + j < 6:
            diagonal_list.append(self.__board_list[y_index - i + j][x_index - i + j])
            j += 1

        return diagonal_list

    def __get_diagonal_2_list(self, x_index, y_index):
        """Get a list of all slots found diagonally from the given indices in the bottom left to top right direction.

        Args:
            x_index (int): The x index of the position where to get the diagonal list from.
            y_index (int): The y index of the position where to get the diagonal list from.

        Returns:
            list: List of all diagonal slots from the given indices.
        """
        i = 0
        while x_index - i > 0 and y_index + i < 5:
            i += 1

        diagonal_list = []
        j = 0
        while x_index - i + j < 7 and y_index + i - j >= 0:
            diagonal_list.append(self.__board_list[y_index + i - j][x_index - i + j])
            j += 1

        return diagonal_list

    def __list_contains_4(self, t: list, of):
        """Check if the given list contains four in a row of the given element.

        Args:
            t (list): The list to check.
            of (Any): The elements to check for. Elements will be compared using the == operator.

        Returns:
            tuple: The start and end indices of the line of four.
        """
        count = 0
        start = -1
        end = -1
        for i in range(len(t)):
            if t[i] == of:
                count += 1
            else:
                count = 0

            if count == 1:
                start = i
            elif count == 4:
                end = i
                return (start, end)

        return None

    def count_lines_from(self, x_index, y_index, player):
        """Counts the amount of 2, 3, and 4 sized lines the player has starting from the given indices.

        Args:
            x_index (int): The x index of the starting position.
            y_index (int): The y index of the starting position.
            player (int): Which player to count the lines for. 1 for player 1. 2 for player 2.

        Returns:
            list: A list containing the count of the 2, 3 and 4 sized lines in that order.
        """
        horizontal_list = self.__board_list[y_index]
        horizontal_lines = self.__count_lines(horizontal_list, player)

        vertical_list = self.__get_vertical_list(x_index)
        vertical_lines = self.__count_lines(vertical_list, player)

        diagonal_1_list = self.__get_diagonal_1_list(x_index, y_index)
        diagonal_1_lines = self.__count_lines(diagonal_1_list, player)

        diagonal_2_list = self.__get_diagonal_2_list(x_index, y_index)
        diagonal_2_lines = self.__count_lines(diagonal_2_list, player)

        return [sum(counts) for counts in zip(horizontal_lines, vertical_lines, diagonal_1_lines, diagonal_2_lines)]

    def __count_lines(self, t: list, player):
        """Counts the amount of 2, 3 and 4 sized lines the player has in the given list.

        Args:
            t (list): The list to count the lines from.
            player (int): Which player to count the lines for. 1 for player 1. 2 for player 2.

        Returns:
            tuple: A tuple containing the count of the 2, 3 and 4 sized lines in that order.
        """
        lines_of_2 = 0
        lines_of_3 = 0
        lines_of_4 = 0

        for i in range(len(t) - 3):
            line = "".join(str(x) for x in t[i:i+4])

            if len(re.findall(str(player), line)) == 2 and len(re.findall("0", line)) == 2:
                lines_of_2 += 1

            if len(re.findall(str(player), line)) == 3 and len(re.findall("0", line)) == 1:
                lines_of_3 += 1

            if len(re.findall(str(player), line)) == 4:
                lines_of_4 += 1

        return (lines_of_2, lines_of_3, lines_of_4)

    def get_legal_moves(self):
        """Returns list of all currently possible moves.

        Returns:
            list: The list of all currently possible moves.
        """
        moves = []
        for i in self.get_move_order():
            if self.__board_list[0][i] == 0:
                moves.append(i)

        return moves

    def get_move_order(self):
        return [3, 2, 4, 1, 5, 0, 6]
    
    def __str__(self):
        s = ""
        for row in self.__board_list:
            s += "".join(row)

        return s