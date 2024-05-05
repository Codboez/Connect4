import time
import pygame
from src.ui.board_ui import BoardUI
from src.logic.manager import Manager
from src.ui.visualizer import Visualizer
from src.ui.pause_menu import PauseMenu
from src.logic.board import Board

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen_width = 1280
        self.screen_height = 960
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.font_path = pygame.font.match_font("timesnewroman")
        self.font = pygame.font.Font(self.font_path, 12)
        self.board_ui = BoardUI(self)
        self.visualizer = Visualizer(self, False)
        self.manager = Manager(self.board_ui, self.visualizer)
        self.pause_menu = PauseMenu(self)
        self.running = True
        self.delta_time = 0
        self.__prev_update = time.time()
        self.mouse_pos = (0, 0)

    def render(self):
        """Renders one frame. Called every game loop.
        """
        self.screen.fill((255, 255, 255), (0, 0, self.screen_width, self.screen_height))

        self.board_ui.render(self.screen)
        self.visualizer.render(self.screen)
        self.pause_menu.render(self.screen)

        pygame.display.flip()

    def update(self):
        """Updates the game. Called every game loop.
        """
        self.delta_time = time.time() - self.__prev_update
        self.__prev_update = time.time()
        self.board_ui.update()
        self.pause_menu.update(self.mouse_pos)

    def run(self):
        """Starts the game.
        """
        while self.running:
            self.update()
            self.render()
            self.check_events()

    def check_events(self):
        """Checks for all required pygame events.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.manager.close_all_other_threads()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.pause_menu.enabled:
                    self.pause_menu.mouse_down(event.pos)
                else:
                    self.manager.mouse_down(event.pos)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.pause_menu.enabled = not self.pause_menu.enabled
            elif event.type == pygame.MOUSEMOTION:
                self.mouse_pos = event.pos

    def get_font_with_size(self, size):
        return pygame.font.Font(self.font_path, size)
    
    def reset(self):
        board = Board()
        self.board_ui.board = board
        self.manager.reset(board)