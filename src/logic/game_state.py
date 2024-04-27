class GameState:
    def __init__(self) -> None:
        pass

    def calculate_value_for_player(self, player, board, drop_location):
        """Calculates the value of the state of the game for the player based on the given moves.

        Args:
            player (int): The player to check the value for. 1 for player 1. 2 for player 2.
            board (Board): The Connect Four board.
            drop_location (tuple): The drop location on the board to evaluate.

        Returns:
            int: The value for the player.
        """
        score = 0

        lines = board.count_lines_from(drop_location[0], drop_location[1], player)

        score += lines[1] * 5
        score += lines[0]

        if lines[2] > 0:
            score += 1000

        return score