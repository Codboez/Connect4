import time
from pygame import draw, display

class Visualizer:
    def __init__(self, game, use_visualizer=False) -> None:
        self.enabled = False
        self.__nodes = {}
        self.__game = game
        self.__parent = []
        self.__prev_index = -1
        self.__use_visualizer = use_visualizer
        self.reset()

    def add_value(self, value, depth, index):
        if not self.enabled:
            return

        if depth - 1 < len(self.__parent) and depth != 0:
            self.__parent.pop(-1)

        if depth == 0:
            self.__nodes[()] = (value, self.calculate_position(()))
            return

        self.set_value(index, value)
        time.sleep(0.1)

    def add_node(self, depth, index):
        if not self.enabled:
            return

        if depth - 1 > len(self.__parent):
            self.__parent.append(self.__prev_index)

        self.set_value(index, None)
        self.__prev_index = index

    def render(self, screen):
        if not self.enabled:
            return

        screen.fill((255, 255, 255), (0, 0, self.__game.screen_width, self.__game.screen_height))
        self.render_node(screen, ())

        try:
            for path in list(self.__nodes.keys()):
                self.render_connection(screen, path)

            for path in list(self.__nodes.keys()):
                self.render_node(screen, path)
        except KeyError:
            pass

        display.flip()

    def render_node(self, screen, node_path):
        size = 40 if len(node_path) == 0 else 20 / len(node_path)
        draw.circle(screen, (255, 255, 255), self.get_position(node_path), size)
        draw.circle(screen, (0, 0, 0), self.get_position(node_path), size, 4 - len(node_path))

        value_text = self.__game.font.render(str(self.get_value(node_path)), False, (0, 0, 0))

        position = self.get_position(node_path)
        position = (position[0] - value_text.get_width() / 2, position[1] - value_text.get_height() / 2)
        screen.blit(value_text, position)

    def render_connection(self, screen, node_path):
        draw.line(screen, (0, 0, 0), self.get_parent_position(node_path), self.get_position(node_path))

    def set_value(self, index, value):
        copy_parent = self.__parent.copy()
        copy_parent.append(index)
        path = tuple(copy_parent)
        self.__nodes[path] = (value, self.calculate_position(path))

    def get_parent_position(self, node_path):
        return self.get_position(node_path[:-1])

    def get_position(self, node_path):
        if len(node_path) == 0:
            return (self.__game.screen_width / 2, 150)

        return self.__nodes[node_path][1]

    def get_value(self, node_path):
        return self.__nodes[node_path][0]

    def calculate_position(self, node_path):
        if len(node_path) == 0:
            return (self.__game.screen_width / 2, 150)

        y = (len(node_path) + 1) * 150
        x = self.calculate_parent_position(node_path)[0] + (node_path[-1] - 3) * 1100 / 8**len(node_path)

        return (x, y)

    def calculate_parent_position(self, node_path):
        if len(node_path) == 0:
            return None

        parent_path = node_path[:-1]
        return self.calculate_position(parent_path)

    def set_enabled(self, enabled):
        if not self.__use_visualizer:
            return
        time.sleep(1)
        self.enabled = enabled
        self.reset()

    def reset(self):
        self.__nodes = {}
        self.__nodes[()] = (None, self.get_position(()))