import time
import pygame
from src.ui.board_ui import BoardUI
from src.logic.manager import Manager
from src.ui.visualizer import Visualizer

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen_width = 960
        self.screen_height = 720
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.font = pygame.font.SysFont("timesnewroman", 12)
        self.board_ui = BoardUI(self)
        self.visualizer = Visualizer(self, False)
        self.manager = Manager(self.board_ui, self.visualizer)
        self.running = True
        self.delta_time = 0
        self.__prev_update = time.time()

    def render(self):
        """Renders one frame. Called every game loop.
        """
        self.screen.fill((255, 255, 255), (0, 0, self.screen_width, self.screen_height))

        self.board_ui.render(self.screen)
        self.visualizer.render(self.screen)

        pygame.display.flip()

    def update(self):
        """Updates the game. Called every game loop.
        """
        self.delta_time = time.time() - self.__prev_update
        self.__prev_update = time.time()
        self.board_ui.update()

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
                self.manager.mouse_down(event.pos)