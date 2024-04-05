import threading
import random
from src.logic.controller import Controller
from src.logic.game_state import GameState

class AI(Controller):
    def __init__(self, index, board_ui, manager) -> None:
        self.__index = index
        self.__board_ui = board_ui
        self.__board = board_ui.board
        self.__manager = manager

    def start_turn(self):
        ai_thread = threading.Thread(target=self.calculate_best_move)
        ai_thread.start()

    def calculate_best_move(self):
        best_list = []
        for i in range(7):
            alpha = -10**6
            value = self.minimax(1, 7, [i], alpha, 10**6)
            alpha = max(alpha, value)
            best_list.append(value)

        best_move = self.get_index_of_best(best_list)
        self.__board_ui.drop_to_column(best_move, self.__index)
        self.__manager.end_turn()

    def minimax(self, k, n, done_moves, alpha, beta):
        if k == n:
            game_state = GameState()

            try:
                value = game_state.calculate_value_for_player(self.__index, self.__board, done_moves)
            except ValueError:
                return 0 if k % 2 == 1 else 10**5

            return value

        best = 0 if k % 2 == 0 else 10**5
        for i in range(7):
            new_done_moves = done_moves.copy()
            new_done_moves.append(i)
            value = self.minimax(k + 1, n, new_done_moves, alpha, beta)
            best = max(best, value) if k % 2 == 0 else min(best, value)
            
            if k % 2 == 0:
                alpha = max(alpha, value)
            else:
                beta = min(beta, value)

            if alpha >= beta:
                break

        return 0 if best == 10**5 else best

    def get_index_of_best(self, best_list):
        best = (0, -1)
        for i in range(len(best_list)):
            if best_list[i] > best[0]:
                best = (best_list[i], i)

        if best[1] == -1:
            legal_moves = self.__board.get_legal_moves()
            return legal_moves[random.randint(0, len(legal_moves) - 1)]

        return best[1]