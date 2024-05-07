from src.logic.player import Player
from src.logic.ai import AI

class Manager:
    def __init__(self, board_ui, visualizer) -> None:
        self.__board_ui = board_ui
        self.controllers = [Player(), AI(2, self.__board_ui.board, self, 2, visualizer, True)]
        self.current_turn = 0
        self.active = True
        self.set_turn(0)

    def mouse_down(self, pos):
        """This is called when mouse is clicked. Advances the game if it was a player's turn.

        Args:
            pos (tuple): The mouse position on the screen when mouse was clicked.
        """

        if not self.active:
            return

        if isinstance(self.controllers[self.current_turn], Player):
            column = self.__board_ui.get_column(pos)
            self.end_turn(column)

    def set_turn(self, turn):
        """Gives the turn to the given controller index.

        Args:
            turn (int): The index of the controller the turn is given to. 1 for player 1. 2 for player 2.
        """
        self.current_turn = turn

        if isinstance(self.controllers[turn], AI):
            self.controllers[turn].start_turn()

    def end_turn(self, column):
        """Ends the current controller's turn. Ends the game upon win. Gives the other controller the turn otherwise.

        Args:
            column (int): The index of the column to drop a coin into.
        """
        if not self.__board_ui.drop_to_column(column, self.current_turn + 1):
            return

        winning_line = self.__board_ui.board.check_win(self.current_turn + 1)

        if winning_line is None:
            self.set_turn(1 - self.current_turn)
        else:
            self.__board_ui.winning_line = winning_line
            self.active = False

    def close_all_other_threads(self):
        """Closes all AI threads.
        """
        if isinstance(self.controllers[0], AI):
            self.controllers[0].stop_ai_thread = True

        if isinstance(self.controllers[1], AI):
            self.controllers[1].stop_ai_thread = True

    def reset(self, board):
        if isinstance(self.controllers[0], AI):
            self.controllers[0].set_board(board)

        if isinstance(self.controllers[1], AI):
            self.controllers[1].set_board(board)

        self.set_turn(0)
        self.active = True
        self.__board_ui.winning_line = None

    def get_ai_settings(self):
        settings = []
        if isinstance(self.controllers[0], AI):
            settings.append(self.controllers[0].get_settings())

        if isinstance(self.controllers[1], AI):
            settings.append(self.controllers[1].get_settings())

        return settings