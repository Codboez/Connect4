from pygame import draw
from src.logic.board import Board

class BoardUI:
    def __init__(self, game) -> None:
        self.__game = game
        self.board = Board()
        self.__board_width = self.__game.screen_width - 300
        self.__board_height = self.__board_width * 6 / 7
        self.__board_position = (150, 100)
        self.__circle_radius = self.__board_width / 18
        self.__gap_size = 2 / 72 * self.__board_width
        self.__column_size = self.__circle_radius * 2 + self.__gap_size
        self.__active_coins = {}
        self.winning_line = None

    def render(self, screen):
        """Renders one frame of the Connect Four board. Called every frame.

        Args:
            screen (pygame.Surface): The main surface the game is rendered on.
        """

        rect = (self.__board_position[0], self.__board_position[1], self.__board_width, self.__board_height)
        screen.fill((0, 0, 225), rect)

        self.render_slots(screen)
        self.render_active(screen)
        self.render_winning_line(screen)

    def update(self):
        """Updates any movement on the board. Called each game update.
        """

        self.move_active_coins()

    def move_active_coins(self):
        """Moves recently dropped coins.
        """

        to_delete = []

        for board_indices, screen_y in self.__active_coins.items():
            self.__active_coins[board_indices] = screen_y + 2000 * self.__game.delta_time

            if self.__active_coins[board_indices] >= self.get_center_y(board_indices[1]):
                to_delete.append(board_indices)

        self.__delete_from_dict(to_delete, self.__active_coins)

    def __delete_from_dict(self, to_delete, dictionary):
        for current in to_delete:
            del dictionary[current]

    def render_slots(self, screen):
        """Renders each of the circles on the board.

        Args:
            screen (pygame.Surface): The main surface the game is rendered on.
        """

        for y in range(6):
            for x in range(7):
                if (x, y) in self.__active_coins:
                    color = (255, 255, 255)
                else:
                    color = self.get_player_color(self.board.get_slot(x, y))

                center_x = self.get_center_x(x)
                center_y = self.get_center_y(y)
                draw.circle(screen, color, (center_x, center_y), self.__circle_radius)

    def render_active(self, screen):
        """Renders all recently dropped coins (still moving).

        Args:
            screen (pygame.Surface): The main surface the game is rendered on.
        """

        for board_indices, screen_y in self.__active_coins.items():
            color = self.get_player_color(self.board.get_slot(board_indices[0], board_indices[1]))

            center_x = self.get_center_x(board_indices[0])
            draw.circle(screen, color, (center_x, screen_y), self.__circle_radius)

    def render_winning_line(self, screen):
        """Renders a line on top of a line of four connected coins if one exists.

        Args:
            screen (pygame.Surface): The main surface the game is rendered on.
        """

        if self.winning_line is None:
            return

        # pylint: disable=unsubscriptable-object
        # It is subscriptable when it is not None (Which is checked above).

        start = (self.get_center_x(self.winning_line[0][0]), self.get_center_y(self.winning_line[0][1]))
        end = (self.get_center_x(self.winning_line[1][0]), self.get_center_y(self.winning_line[1][1]))
        draw.line(screen, (0, 0, 0), start, end, 8)

    def get_center_x(self, index):
        """Gets the x coordinate of the center position of the given column index.

        Args:
            index (int): The index of the column of whose center x position is returned.

        Returns:
            float: The x coordinate of the given column's center position.
        """

        return self.__board_position[0] + self.__circle_radius + self.__gap_size + index * self.__column_size

    def get_center_y(self, index):
        """Gets the y coordinate of the center position of the given row index.

        Args:
            index (int): The index of the row of whose center y position is returned.

        Returns:
            float: The y coordinate of the given row's center position.
        """

        return self.__board_position[1] + self.__circle_radius + self.__gap_size + index * self.__column_size

    def get_player_color(self, player):
        """Gets the color of coins based on the given player index.

        Args:
            player (int): The index of the player whose color to get. 1 for player 1. 2 for player 2. 0 for empty.

        Raises:
            ValueError: Raised if given player is invalid: Not an integer between 0 and 2.

        Returns:
            tuple: Color containing RGB values.
        """

        if player == 0:
            return (255, 255, 255)

        if player == 1:
            return (255, 255, 0)

        if player == 2:
            return (255, 0, 0)

        raise ValueError("Invalid player")

    def get_column(self, pos):
        """Gets the index of the column on the board where the mouse is in.

        Args:
            pos (tuple): The current mouse position.

        Returns:
            int: The index of the found column. -1 if not found.
        """

        if pos[0] < self.__board_position[0] or pos[0] > self.__board_position[0] + self.__board_width:
            return -1

        pos_x = pos[0] - self.__board_position[0]

        return int(pos_x // self.__column_size)

    def drop(self, pos, controller_number):
        """Tries to drop a coin based on the given mouse position.

        Args:
            pos (tuple): The current mouse position.
            controller_number (int): The index of the controller whose color to get. 1 for player 1. 2 for player 2.

        Returns:
            bool: If a drop was completed.
        """

        x = self.get_column(pos)
        return self.drop_to_column(x, controller_number)

    def drop_to_column(self, column, controller_number):
        """Tries to drop a coin in the given column.

        Args:
            column (int): The index of the column to drop a coin into.
            controller_number (int): The index of the controller whose color to get. 1 for player 1. 2 for player 2.

        Returns:
            bool: If a drop was completed.
        """
        if column == -1:
            return False

        try:
            board_indices = self.board.drop(column, controller_number)
            self.__active_coins[board_indices] = 50
        except ValueError:
            return False

        return True