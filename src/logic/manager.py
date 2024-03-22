from logic.controller import Controller
from logic.player import Player
from logic.ai import AI

class Manager:
    def __init__(self, board_UI) -> None:
        self.__board_UI = board_UI
        self.controllers = [Player(), Player()]
        self.current_turn = 0
        self.active = True

    def mouse_down(self, pos):
        if not self.active:
            return

        if isinstance(self.controllers[self.current_turn], Player):
            if self.__board_UI.drop(pos, self.current_turn + 1):
                winning_line = self.__board_UI.board.check_win(self.current_turn + 1)

                if winning_line is None:
                    self.set_turn(1 - self.current_turn)
                else:
                    self.__board_UI.winning_line = winning_line
                    self.active = False

    def set_turn(self, turn):
        self.current_turn = turn

        if self.controllers[turn] is AI:
            self.controllers[turn].start_turn()