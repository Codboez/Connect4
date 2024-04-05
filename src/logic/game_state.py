class GameState:
    def __init__(self) -> None:
        pass

    def calculate_value_for_player(self, player, board, moves):
        new_board = board.copy()
        other_player = 3 - player

        for i in range(len(moves)):
            next_player = player if i % 2 == 0 else other_player
            drop_location = new_board.drop(moves[i], next_player)

            if new_board.four_in_line_from(next_player, drop_location[0], drop_location[1]) is not None:
                return 10 if next_player == player else 0

        return 5