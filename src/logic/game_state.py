import random

class GameState:
    def __init__(self) -> None:
        pass

    def calculate_value_for_player(self, player, board, moves):
        new_board = self.create_state(board, moves, player) # pylint: disable=unused-variable

        return random.randint(1, 10)

    def create_state(self, board, moves, player):
        new_board = board.copy()
        other_player = 3 - player

        for i in range(len(moves)):
            next_player = player if i % 2 == 0 else other_player
            new_board.drop(moves[i], next_player)

        return new_board