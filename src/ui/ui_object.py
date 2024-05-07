from pygame import draw

class UIObject:
    def __init__(self, position, size, color, text, font, hover_color=None,
                 border_color=(0, 0, 0), text_color=(0, 0, 0)) -> None:
        self.size = size
        self.color = color
        self.position = position
        self.hovered = False
        self.text = text
        self.font = font
        self.border_color = border_color
        self.text_color = text_color

        if hover_color is None:
            self.hover_color = self.make_darker(color)
        else:
            self.hover_color = hover_color

    def make_darker(self, color, amount=25):
        return (max(color[0] - amount, 0), max(color[1] - amount, 0), max(color[2] - amount, 0))

    def make_lighter(self, color, amount=25):
        return (min(color[0] + amount, 255), min(color[1] + amount, 255), min(color[2] + amount, 255))

    def click(self):
        pass

    def unclick(self):
        pass

    def is_inside(self, pos):
        return (pos[0] > self.position[0] and pos[0] < self.position[0] + self.size[0]
                     and pos[1] > self.position[1] and pos[1] < self.position[1] + self.size[1])

    def render(self, screen):
        self.render_background(screen)
        self.render_text(screen)
        self.render_border(screen)

    def render_text(self, screen):
        text = self.font.render(self.text, True, self.text_color)
        position = (self.position[0] + self.size[0] / 2 - text.get_width() / 2,
                    self.position[1] + self.size[1] / 2 - text.get_height() / 2)
        screen.blit(text, position)

    def render_border(self, screen):
        draw.aaline(screen, self.border_color, self.position, (self.position[0] + self.size[0], self.position[1]))
        draw.aaline(screen, self.border_color, self.position, (self.position[0], self.position[1] + self.size[1]))
        draw.aaline(screen, self.border_color, (self.position[0] + self.size[0], self.position[1] + self.size[1]),
                    (self.position[0] + self.size[0], self.position[1]))
        draw.aaline(screen, self.border_color, (self.position[0] + self.size[0], self.position[1] + self.size[1]),
                    (self.position[0], self.position[1] + self.size[1]))

    def render_background(self, screen):
        background_color = self.hover_color if self.hovered else self.color
        screen.fill(background_color, (self.position[0], self.position[1], self.size[0], self.size[1]))

    def update(self, mouse_pos):
        self.hovered = self.is_inside(mouse_pos)