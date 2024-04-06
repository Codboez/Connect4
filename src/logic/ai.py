import threading
import random
from src.logic.controller import Controller
from src.logic.game_state import GameState

class AI(Controller):
    def __init__(self, index, board, manager, max_depth) -> None:
        self.__index = index
        self.__board = board
        self.__manager = manager
        self.__max_depth = 1
        self.stop_ai_thread = False
        self.set_max_depth(max_depth)

    def start_turn(self):
        ai_thread = threading.Thread(target=self.calculate_best_move)
        ai_thread.start()

    def calculate_best_move(self):
        best_list = []
        alpha = -10**6
        for i in range(7):
            value = self.minimax(1, self.__max_depth, [i], alpha, 10**6)

            if value is None:
                best_list.append(value)
                continue

            alpha = max(alpha, value)
            best_list.append(value)

        best_move = self.get_index_of_best(best_list)
        self.__manager.end_turn(best_move)

    def minimax(self, k, n, done_moves, alpha, beta):
        if k == n:
            game_state = GameState()

            try:
                value = game_state.calculate_value_for_player(self.__index, self.__board, done_moves)
            except ValueError:
                return None

            return value

        best = None

        for i in range(7):
            if self.stop_ai_thread:
                return None

            new_done_moves = done_moves.copy()
            new_done_moves.append(i)
            value = self.minimax(k + 1, n, new_done_moves, alpha, beta)

            if value is None:
                continue

            if best is None:
                best = value

            best = max(best, value) if k % 2 == 0 else min(best, value)

            if k % 2 == 0:
                alpha = max(alpha, value)
            else:
                beta = min(beta, value)

            if alpha >= beta:
                break

        return best

    def get_index_of_best(self, best_list):
        best = (0, -1)
        for i in range(len(best_list)):
            if best_list[i] is None:
                continue

            if best_list[i] > best[0]:
                best = (best_list[i], i)

        if best[1] == -1:
            print("Every move resulted in a loss (assuming player plays perfectly). Random move chosen.")
            legal_moves = self.__board.get_legal_moves()
            return legal_moves[random.randint(0, len(legal_moves) - 1)]

        return best[1]

    def set_max_depth(self, depth):
        if depth < 1:
            raise ValueError("Maximum depth cannot be less than 1.")

        self.__max_depth = depth