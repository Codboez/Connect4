from src.ui.ui_object import UIObject

class Button(UIObject):
    def __init__(self, position, size, color, text, font, action, args=[], hover_color=None,
                 border_color=(0, 0, 0), text_color=(0, 0, 0)) -> None:
        super().__init__(position, size, color, text, font, hover_color, border_color, text_color)
        self.action = action
        self.args = args
    
    def click(self):
        self.action(*self.args)