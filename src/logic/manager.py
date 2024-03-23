from src.logic.player import Player
from src.logic.ai import AI

class Manager:
    def __init__(self, board_ui) -> None:
        self.__board_ui = board_ui
        self.controllers = [Player(), Player()]
        self.current_turn = 0
        self.active = True

    def mouse_down(self, pos):
        """This is called when mouse is clicked. Advances the game if it was a player's turn.

        Args:
            pos (tuple): The mouse position on the screen when mouse was clicked.
        """

        if not self.active:
            return

        if isinstance(self.controllers[self.current_turn], Player):
            if self.__board_ui.drop(pos, self.current_turn + 1):
                winning_line = self.__board_ui.board.check_win(self.current_turn + 1)

                if winning_line is None:
                    self.set_turn(1 - self.current_turn)
                else:
                    self.__board_ui.winning_line = winning_line
                    self.active = False

    def set_turn(self, turn):
        """Gives the turn to the given controller index.

        Args:
            turn (int): The index of the controller the turn is given to. 1 for player 1. 2 for player 2.
        """
        self.current_turn = turn

        if self.controllers[turn] is AI:
            self.controllers[turn].start_turn()