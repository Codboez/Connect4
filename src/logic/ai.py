import threading
import random
from src.logic.controller import Controller
from src.logic.game_state import GameState

class AI(Controller):
    def __init__(self, index, board, manager, max_depth, use_alpha_beta=True) -> None:
        self.__index = index
        self.__board = board
        self.__manager = manager
        self.__max_depth = 1
        self.stop_ai_thread = False
        self.use_alpha_beta = use_alpha_beta
        self.set_max_depth(max_depth)

    def start_turn(self, create_new_thread = True):
        """Starts the AI's calculations for its move. The calculations will be done in a new thread.
        """
        if create_new_thread:
            ai_thread = threading.Thread(target=self.calculate_best_move)
            ai_thread.start()
        else:
            self.calculate_best_move()

    def calculate_best_move(self):
        """Calculates the best possible move the AI can make and drops a coin there.
        """
        best_move = self.start_minimax()
        self.__manager.end_turn(best_move)

    def start_minimax(self):
        """Starts the minimax algorithm.

        Returns:
            int: The index of the column the best move was found in.
        """
        best_list = []
        alpha = -10**6
        for i in self.get_move_order():
            value = self.minimax(1, self.__max_depth, [i], alpha, 10**6)

            if value is None:
                best_list.append((value, i))
                continue

            alpha = max(alpha, value)
            best_list.append((value, i))

        best_move = self.get_index_of_best(best_list)
        return best_move

    def minimax(self, depth, max_depth, done_moves, alpha, beta):
        """The minimax algorithm. Calculates the best possible move the AI can make.

        Args:
            depth (int): The current depth.
            max_depth (int): The maximum depth
            done_moves (list): List of moves (column indices) that are going to be evaluated.
            alpha (int): The alpha value for alpha-beta pruning.
            beta (int): The beta value for alpha-beta pruning.

        Returns:
            int: The value of the best move.
        """
        if depth == max_depth:
            return self.calculate_value_for_game_state(done_moves)

        best = None

        for i in self.get_move_order():
            if self.stop_ai_thread:
                return None

            new_done_moves = done_moves.copy()
            new_done_moves.append(i)
            value = self.minimax(depth + 1, max_depth, new_done_moves, alpha, beta)

            if value is None:
                continue

            if best is None:
                best = value

            best = max(best, value) if depth % 2 == 0 else min(best, value)

            if depth % 2 == 0:
                alpha = max(alpha, value)
            else:
                beta = min(beta, value)

            if self.use_alpha_beta and alpha >= beta:
                break

        return best

    def calculate_value_for_game_state(self, moves):
        """Calculates the value of the state of the game based on the given moves.

        Args:
            moves (int): List of moves (column indices) that are being evaluated.

        Returns:
            int: The value for the AI.
        """
        game_state = GameState()

        try:
            value = game_state.calculate_value_for_player(self.__index, self.__board, moves)
        except ValueError:
            return None

        return value

    def get_index_of_best(self, best_list):
        """Get the column index for the best move. 

        Args:
            best_list (list): List of values for each move

        Returns:
            int: The column index of the best move.
        """
        best = (-10000, -1)
        for i in range(len(best_list)):
            if best_list[i][0] is None:
                continue

            if best_list[i][0] > best[0]:
                best = (best_list[i][0], best_list[i][1])

        if best[1] == -1:
            legal_moves = self.__board.get_legal_moves()
            return legal_moves[random.randint(0, len(legal_moves) - 1)]

        return best[1]

    def set_max_depth(self, depth):
        if depth < 1:
            raise ValueError("Maximum depth cannot be less than 1.")

        self.__max_depth = depth

    def get_move_order(self):
        return [3, 2, 4, 1, 5, 0, 6]