import threading
import random
import time
from src.logic.controller import Controller
from src.logic.game_state import GameState

class AI(Controller):
    def __init__(self, index, board, manager, max_depth, visualizer, use_alpha_beta=True) -> None:
        self.__index = index
        self.__board = board
        self.__manager = manager
        self.__max_depth = 1
        self.stop_ai_thread = False
        self.use_alpha_beta = use_alpha_beta
        self.__visualizer = visualizer
        self.set_max_depth(max_depth)

    def start_turn(self, create_new_thread=True, use_iterative_deepening=True):
        """Starts the AI's calculations for its move.

        Args:
            create_new_thread (bool): Whether to do the calculations in a new thread or the main thread.
            use_iterative_deepening (bool): Whether to use iterative deepening or not.
        """
        if create_new_thread:
            ai_thread = threading.Thread(target=self.calculate_best_move, args=[use_iterative_deepening])
            ai_thread.start()
        else:
            self.calculate_best_move(use_iterative_deepening)

    def calculate_best_move(self, use_iterative_deepening=True):
        """Calculates the best possible move the AI can make and drops a coin there.

        Args:
            use_iterative_deepening (bool): Whether to use iterative deepening or not.
        """
        self.__visualizer.set_enabled(True)

        if use_iterative_deepening:
            best_move = self.start_iterative_deepening()
        else:
            _, best_move = self.minimax(0, self.__max_depth, [], -10**6, 10**6)
        
        self.__manager.end_turn(best_move)
        self.__visualizer.set_enabled(False)

    # Obsolete method
    def start_minimax(self, max_depth):
        """Starts the minimax algorithm.

        Args:
            max_depth (int): The maximum depth.

        Returns:
            int: The index of the column the best move was found in.
        """
        best_list = []
        alpha = -10**6
        for i in self.__board.get_legal_moves():
            self.__visualizer.add_node(1, i)
            value = self.minimax(1, max_depth, [i], alpha, 10**6)
            self.__visualizer.add_value(value, 1, i)

            if value is None:
                best_list.append((value, i))
                continue

            alpha = max(alpha, value)
            best_list.append((value, i))

        best_move = self.get_index_of_best(best_list)
        return best_move
    
    def start_iterative_deepening(self, time_limit=3):
        start_time = time.time()
        i = 1
        column = None
        while time.time() - start_time < time_limit:
            _, new_column = self.minimax(0, i, [], -10**6, 10**6)

            if new_column is None:
                return column

            column = new_column
            i += 1

        return column

    def minimax(self, depth, max_depth, done_moves, alpha, beta):
        """The minimax algorithm. Calculates the best possible move the AI can make.

        Args:
            depth (int): The current depth.
            max_depth (int): The maximum depth.
            done_moves (list): List of moves (column indices) that are going to be evaluated.
            alpha (int): The alpha value for alpha-beta pruning.
            beta (int): The beta value for alpha-beta pruning.

        Returns:
            tuple: The value and the column of the best move.
        """
        if depth == max_depth:
            return (self.calculate_value_for_game_state(done_moves), None)

        best = None
        column = None

        for i in self.__board.get_legal_moves():
            if self.stop_ai_thread:
                return (None, None)

            new_done_moves = done_moves.copy()
            new_done_moves.append(i)
            self.__visualizer.add_node(depth + 1, i)
            value, _ = self.minimax(depth + 1, max_depth, new_done_moves, alpha, beta)
            self.__visualizer.add_value(value, depth + 1, i)

            if value is None:
                continue

            if best is None:
                best = value
                column = i

            if depth % 2 == 0:
                if value > best:
                    column = i
                    best = value

                alpha = max(alpha, value)
            else:
                if value < best:
                    column = i
                    best = value

                beta = min(beta, value)

            if self.use_alpha_beta and alpha >= beta:
                break

        return (best, column)

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

        self.__visualizer.add_value(best[0], 0, best[1])
        return best[1]

    def set_max_depth(self, depth):
        if depth < 1:
            raise ValueError("Maximum depth cannot be less than 1.")

        self.__max_depth = depth