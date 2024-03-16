from pygame import draw
from logic.board import Board

class BoardUI:
    def __init__(self, game) -> None:
        self.__game = game
        self.__board = Board()
        self.__board_width = self.__game.SCREEN_WIDTH - 300
        self.__board_height = self.__board_width * 6 / 7
        self.__board_position = (150, 100)
        self.__circle_radius = self.__board_width / 18
        self.__gap_size = 2 / 72 * self.__board_width
        self.__column_size = self.__circle_radius * 2 + self.__gap_size

    def render(self, screen):
        screen.fill((0, 0, 225), (self.__board_position[0], self.__board_position[1], self.__board_width, self.__board_height))

        self.render_slots(screen)

    def render_slots(self, screen):
        for y in range(6):
            for x in range(7):
                color = self.get_player_color(self.__board.get_slot(x, y))

                center_x = self.__board_position[0] + self.__circle_radius + self.__gap_size + x * self.__column_size
                center_y = self.__board_position[1] + self.__circle_radius + self.__gap_size + y * self.__column_size
                draw.circle(screen, color, (center_x, center_y), self.__circle_radius)

    def get_player_color(self, player):
        if player == 0:
            return (255, 255, 255)
        
        if player == 1:
            return (255, 255, 0)
        
        if player == 2:
            return (255, 0, 0)
        
        raise ValueError("Invalid player")
    
    def get_column(self, pos):
        if pos[0] < self.__board_position[0] or pos[0] > self.__board_position[0] + self.__board_width:
            return -1
        
        pos_x = pos[0] - self.__board_position[0]

        return int(pos_x // self.__column_size)
    
    def drop(self, pos, controller_number):
        x = self.get_column(pos)

        if x == -1:
            return False
        
        try:
            self.__board.drop(x, controller_number)
        except ValueError:
            return False

        return True