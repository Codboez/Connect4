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
            controller_number (int): Which player to check the win for. 1 for player 1. 2 for player 2.

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
                line_end = self.four_in_line_from(player, x, y)

                if line_end is not None:
                    return ((x, y), line_end)

        return None

    def four_in_line_from(self, player, x_index, y_index):
        """Checks if given player has connected four in any direction starting from the given indices.

        Args:
            player (int): Which player to check the win for. 1 for player 1. 2 for player 2.
            x_index (int): x index of the checked position.
            y_index (int): y index of the checked position.

        Returns:
            tuple: The indices of the position where the winning line ends. Returns None if winning line not found.
        """

        line_end = self.__four_in_line_right(player, x_index, y_index)
        if line_end is not None:
            return line_end

        line_end = self.__four_in_line_down(player, x_index, y_index)
        if line_end is not None:
            return line_end

        line_end = self.__four_in_line_down_right(player, x_index, y_index)
        if line_end is not None:
            return line_end

        line_end = self.__four_in_line_up_right(player, x_index, y_index)
        if line_end is not None:
            return line_end

        return None

    def __four_in_line_right(self, player, x_index, y_index):
        for i in range(4):
            if x_index + i >= len(self.__board_list[y_index]):
                return None

            if self.__board_list[y_index][x_index + i] != player:
                return None

        return (x_index + 3, y_index)

    def __four_in_line_down(self, player, x_index, y_index):
        for i in range(4):
            if y_index + i >= len(self.__board_list):
                return None

            if self.__board_list[y_index + i][x_index] != player:
                return None

        return (x_index, y_index + 3)

    def __four_in_line_down_right(self, player, x_index, y_index):
        for i in range(4):
            if x_index + i >= len(self.__board_list[y_index]) or y_index + i >= len(self.__board_list):
                return None

            if self.__board_list[y_index + i][x_index + i] != player:
                return None

        return (x_index + 3, y_index + 3)

    def __four_in_line_up_right(self, player, x_index, y_index):
        for i in range(4):
            if x_index + i >= len(self.__board_list[y_index]) or y_index - i < 0:
                return None

            if self.__board_list[y_index - i][x_index + i] != player:
                return None

        return (x_index + 3, y_index - 3)

    def copy(self):
        copy_board = Board()

        copy_list = []
        for row in self.__board_list:
            copy_list.append(row.copy())

        copy_board.__board_list = copy_list # pylint: disable=protected-access,unused-private-member
        return copy_board

    def __repr__(self):
        return self.__board_list.__repr__()