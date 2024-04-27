import threading
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
            _, best_move = self.minimax(0, self.__max_depth, self.__board, -10**6, 10**6, None, 0)

        self.__manager.end_turn(best_move)
        self.__visualizer.set_enabled(False)

    def start_iterative_deepening(self, time_limit=3):
        start_time = time.time()
        i = 1
        column = None
        while time.time() - start_time < time_limit:
            if self.stop_ai_thread:
                return (None, None)

            _, column = self.minimax(0, i, self.__board, -10**6, 10**6, None, 0)
            print(i)

            i += 1

        return column

    def minimax(self, depth, max_depth, board, alpha, beta, drop_location, current_score):
        """The minimax algorithm. Calculates the best possible move the AI can make.

        Args:
            depth (int): The current depth.
            max_depth (int): The maximum depth.
            board (Board): The Connect Four board.
            alpha (int): The alpha value for alpha-beta pruning.
            beta (int): The beta value for alpha-beta pruning.
            drop_location (tuple): The drop location on the board to evaluate.
            current_score (int): The currently given score based on previous moves.

        Returns:
            tuple: The value and the column of the best move.
        """
        next_player = self.__index if depth % 2 == 1 else 3 - self.__index
        legal_moves = board.get_legal_moves()

        score = self.calculate_value_for_game_state(board, next_player, drop_location, current_score)

        if next_player == self.__index:
            current_score += score
        else:
            current_score -= score

        if depth == max_depth or score >= 1000 or len(legal_moves) == 0:
            return (current_score, None)

        best = None
        column = None
        next_player = 3 - next_player

        for i in legal_moves:
            new_board = board.copy()
            try:
                drop_location = new_board.drop(i, next_player)
            except ValueError:
                continue

            self.__visualizer.add_node(depth + 1, i)
            value, _ = self.minimax(depth + 1, max_depth, new_board, alpha, beta, drop_location, current_score)
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

    def calculate_value_for_game_state(self, board, player, drop_location, current_score):
        """Calculates the value of the state of the game based on the given moves.

        Args:
            board (Board): The Connect Four board.
            player (int): The player to check the value for. 1 for player 1. 2 for player 2.
            drop_location (tuple): The drop location on the board to evaluate.
            current_score (int): The currently given score based on previous moves.

        Returns:
            int: The value for the AI.
        """
        if drop_location is None:
            return current_score

        game_state = GameState()

        value = game_state.calculate_value_for_player(player, board, drop_location)

        return value

    def set_max_depth(self, depth):
        if depth < 1:
            raise ValueError("Maximum depth cannot be less than 1.")

        self.__max_depth = depth