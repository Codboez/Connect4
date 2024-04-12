class GameState:
    def __init__(self) -> None:
        pass

    def calculate_value_for_player(self, player, board, moves):
        """Calculates the value of the state of the game for the player based on the given moves.

        Args:
            player (int): The player to check the value for. 1 for player 1. 2 for player 2.
            board (Board): The Connect Four board.
            moves (list): List of moves (column indices) that are being evaluated.

        Returns:
            int: The value for the player.
        """
        new_board = board.copy()
        other_player = 3 - player
        score = 0

        for i in range(len(moves)):
            next_player = player if i % 2 == 0 else other_player
            drop_location = new_board.drop(moves[i], next_player)
            
            lines = new_board.count_lines_from(drop_location[0], drop_location[1])

            if lines[3 * (player - 1) + 2] > 0:
                return score + 1000
            
            if lines[3 * (other_player - 1) + 2] > 0:
                return score - 1000
            
            score += lines[3 * (player - 1) + 1] * 5
            score += lines[3 * (player - 1)]

        return score