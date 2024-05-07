from pygame import Surface, SRCALPHA
from src.ui.button import Button
from src.ui.check_box import CheckBox
from src.ui.input_field import InputField

class PauseMenu:
    def __init__(self, game) -> None:
        self.enabled = False
        self.__game = game
        self.__objects = []
        self.__ai_settings = self.__game.manager.get_ai_settings()
        self.create_objects()

    def create_objects(self):
        font = self.__game.get_font_with_size(22)
        font_small = self.__game.get_font_with_size(11)

        position = (self.__game.screen_width / 2 - 50, self.__game.screen_height / 2 - 25)
        new_game = Button(position, (100, 50), (220, 220, 220), "New game", font, self.__game.reset)
        self.__objects.append(new_game)

        position = (self.__game.screen_width / 2 - 50, self.__game.screen_height / 2 + 50)
        action = self.__game.visualizer.flip_use_visualizer
        visualization = CheckBox(position, (25, 25), (240, 240, 240), "Visualization", font, False, action)
        self.__objects.append(visualization)

        position = (self.__game.screen_width / 2 - 50, self.__game.screen_height / 2 + 85)
        action = self.__ai_settings[0].flip_iterative_deepening
        iterative_deepening = CheckBox(position, (25, 25), (240, 240, 240), "Iterative deepening", font,
                                       self.__ai_settings[0].iterative_deepening, action)
        self.__objects.append(iterative_deepening)

        position = (self.__game.screen_width / 2 - 50, self.__game.screen_height / 2 + 120)
        action = self.__ai_settings[0].flip_alpha_beta
        alpha_beta = CheckBox(position, (25, 25), (240, 240, 240), "Alpha-beta pruning", font,
                              self.__ai_settings[0].alpha_beta, action)
        self.__objects.append(alpha_beta)

        position = (self.__game.screen_width / 2 - 50, self.__game.screen_height / 2 + 155)
        action = self.__ai_settings[0].flip_order_moves
        move_ordering = CheckBox(position, (25, 25), (240, 240, 240), "Move ordering", font,
                                 self.__ai_settings[0].order_moves, action)
        self.__objects.append(move_ordering)

        position = (self.__game.screen_width / 2 - 50, self.__game.screen_height / 2 + 190)
        depth = InputField(position, (90, 30), (255, 255, 255), "Minimax depth", font_small)
        self.__objects.append(depth)

        position = (self.__game.screen_width / 2 + 50, self.__game.screen_height / 2 + 190)
        apply_depth = Button(position, (50, 30), (220, 220, 220), "Apply",
                             font_small, lambda: self.__apply_depth(depth))
        self.__objects.append(apply_depth)

        position = (self.__game.screen_width / 2 - 50, self.__game.screen_height / 2 + 225)
        visualization_speed = InputField(position, (90, 30), (255, 255, 255), "Visualization speed", font_small)
        self.__objects.append(visualization_speed)

        position = (self.__game.screen_width / 2 + 50, self.__game.screen_height / 2 + 225)
        apply_speed = Button(position, (50, 30), (220, 220, 220), "Apply", font_small,
                             lambda: self.__apply_speed(visualization_speed))
        self.__objects.append(apply_speed)

    def update(self, mouse_pos):
        for ui_object in self.__objects:
            try:
                ui_object.update(mouse_pos)
            except AttributeError:
                continue

    def render(self, screen):
        if not self.enabled:
            return

        surface = Surface((self.__game.screen_width, self.__game.screen_height), flags=SRCALPHA)
        surface.fill((125, 125, 125, 150), (0, 0, self.__game.screen_width, self.__game.screen_height))

        screen.blit(surface, (0, 0))

        self.render_objects(screen)

    def render_objects(self, screen):
        for ui_object in self.__objects:
            try:
                ui_object.render(screen)
            except AttributeError:
                continue

    def mouse_down(self, pos):
        for ui_object in self.__objects:
            try:
                if ui_object.is_inside(pos):
                    ui_object.click()
                else:
                    ui_object.unclick()
            except AttributeError:
                continue

    def key_down(self, key):
        for ui_object in self.__objects:
            try:
                ui_object.key_down(key)
            except AttributeError:
                continue

    def __apply_depth(self, depth_field):
        self.__ai_settings[0].set_max_depth(depth_field.get_text)

    def __apply_speed(self, speed_field):
        self.__game.visualizer.set_speed(speed_field.get_text)