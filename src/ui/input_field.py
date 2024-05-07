from src.ui.ui_object import UIObject

class InputField(UIObject):
    def __init__(self, position, size, color, placeholder, font, border_color=(0, 0, 0), text_color=(0, 0, 0)) -> None:
        super().__init__(position, size, color, "", font, color, border_color, text_color)
        self.placeholder = placeholder
        self.focused = False

    def render_text(self, screen):
        if self.text == "" and not self.focused:
            text_color = self.make_lighter(self.text_color, 50)
            text = self.font.render(self.placeholder, True, text_color)
        else:
            text_color = self.text_color
            text = self.font.render(self.text, True, text_color)

        position = (self.position[0] + self.size[0] / 2 - text.get_width() / 2,
                    self.position[1] + self.size[1] / 2 - text.get_height() / 2)
        screen.blit(text, position)

    def click(self):
        self.focused = True

    def unclick(self):
        self.focused = False

    def key_down(self, key):
        if not self.focused:
            return

        if key == "\b":
            if len(self.text) > 0:
                self.text = self.text[:-1]
        else:
            self.text += key

    def get_text(self):
        return self.text
