from pygame import draw
from logic.board import Board

class BoardUI:
    def __init__(self, game) -> None:
        self.__game = game
        self.board = Board()
        self.__board_width = self.__game.SCREEN_WIDTH - 300
        self.__board_height = self.__board_width * 6 / 7
        self.__board_position = (150, 100)
        self.__circle_radius = self.__board_width / 18
        self.__gap_size = 2 / 72 * self.__board_width
        self.__column_size = self.__circle_radius * 2 + self.__gap_size
        self.__active_coins = {}
        self.winning_line = None

    def render(self, screen):
        screen.fill((0, 0, 225), (self.__board_position[0], self.__board_position[1], self.__board_width, self.__board_height))

        self.render_slots(screen)
        self.render_active(screen)
        self.render_winning_line(screen)

    def update(self):
        to_delete = []

        for board_indices, screen_y in self.__active_coins.items():
            self.__active_coins[board_indices] = screen_y + 1500 * self.__game.delta_time

            if self.__active_coins[board_indices] >= self.get_center_y(board_indices[1]):
                to_delete.append(board_indices)

        for indices in to_delete:
            del self.__active_coins[indices]

    def render_slots(self, screen):
        for y in range(6):
            for x in range(7):
                if (x, y) in self.__active_coins:
                    color = (255, 255, 255)
                else:
                    color = self.get_player_color(self.board.get_slot(x, y))

                center_x = self.get_center_x(x)
                center_y = self.get_center_y(y)
                draw.circle(screen, color, (center_x, center_y), self.__circle_radius)

    def render_active(self, screen):
        for board_indices, screen_y in self.__active_coins.items():
            color = self.get_player_color(self.board.get_slot(board_indices[0], board_indices[1]))

            center_x = self.get_center_x(board_indices[0])
            draw.circle(screen, color, (center_x, screen_y), self.__circle_radius)

    def render_winning_line(self, screen):
        if self.winning_line is None:
            return
        
        start = (self.get_center_x(self.winning_line[0][0]), self.get_center_y(self.winning_line[0][1]))
        end = (self.get_center_x(self.winning_line[1][0]), self.get_center_y(self.winning_line[1][1]))
        draw.line(screen, (0, 0, 0), start, end, 8)

    def get_center_x(self, index):
        return self.__board_position[0] + self.__circle_radius + self.__gap_size + index * self.__column_size
    
    def get_center_y(self, index):
        return self.__board_position[1] + self.__circle_radius + self.__gap_size + index * self.__column_size

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
            board_indices = self.board.drop(x, controller_number)
            self.__active_coins[board_indices] = 50
        except ValueError:
            return False

        return True