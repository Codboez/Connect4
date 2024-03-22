import pygame
import time
from ui.board_ui import BoardUI
from logic.manager import Manager

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.SCREEN_WIDTH = 960
        self.SCREEN_HEIGHT = 720
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.board_ui = BoardUI(self)
        self.manager = Manager(self.board_ui)
        self.running = True
        self.delta_time = 0
        self.__prev_update = time.time()

    def render(self):
        self.screen.fill((255, 255, 255), (0, 0, self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        self.board_ui.render(self.screen)

        pygame.display.flip()

    def update(self):
        self.delta_time = time.time() - self.__prev_update
        self.__prev_update = time.time()
        self.board_ui.update()

    def run(self):
        while self.running:
            self.update()
            self.render()
            self.check_events()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.manager.mouse_down(event.pos)