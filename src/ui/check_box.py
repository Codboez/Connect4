from pygame import draw
from src.ui.ui_object import UIObject

class CheckBox(UIObject):
    def __init__(self, position, size, color, text, font, enabled, action, args=[], hover_color=None,
                 border_color=(0, 0, 0), text_color=(0, 0, 0)) -> None:
        super().__init__(position, size, color, text, font, hover_color, border_color, text_color)
        self.enabled = enabled
        self.action = action
        self.args = args

    def change_value(self):
        self.enabled = not self.enabled

    def click(self):
        self.change_value()
        self.action(*self.args)

    def render_text(self, screen):
        text = self.font.render(self.text, True, self.text_color)
        position = (self.position[0] + self.size[0] + 10,
                    self.position[1] + self.size[1] / 2 - text.get_height() / 2)
        screen.blit(text, position)

    def render(self, screen):
        self.render_background(screen)
        self.render_text(screen)
        self.render_border(screen)

        if self.enabled:
            self.render_cross(screen)

    def render_cross(self, screen):
        draw.aaline(screen, self.border_color, self.position, 
                    (self.position[0] + self.size[0], self.position[1] + self.size[1]))
        draw.aaline(screen, self.border_color, (self.position[0] + self.size[1], self.position[1]),
                    (self.position[0], self.position[1] + self.size[1]))