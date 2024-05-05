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
        """Adds a value to a node in the given child index of the parent. Determines the parent
        by the given depth and the previously added node with a lower than given depth.

        Args:
            value (int): The value to add to the node.
            depth (int): The depth of the node whose value to add.
            index (int): The child index of the parent.
        """
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
        """Adds a node into the tree. If the depth is higher than that of the previously added node,
        it makes this node the child of the previous node.

        Args:
            depth (int): The depth of this node.
            index (int): The child index of the parent.
        """
        if not self.enabled:
            return

        if depth - 1 > len(self.__parent):
            self.__parent.append(self.__prev_index)

        self.set_value(index, None)
        self.__prev_index = index

    def render(self, screen):
        """Renders the visualizer onto the given screen.

        Args:
            screen (pygame.Surface): The screen the visualizer will be rendered on.
        """
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
        """Renders a node into its location based on the give path of parents to this node.

        Args:
            screen (pygame.Surface): The screen the node will be rendered on.
            node_path (list): The path to the node. A list of column indices of all of this node's parents.
        """
        size = 40 if len(node_path) == 0 else 20 / len(node_path)
        draw.circle(screen, (255, 255, 255), self.get_position(node_path), size)
        draw.circle(screen, (0, 0, 0), self.get_position(node_path), size, 4 - len(node_path))

        value_text = self.__game.font.render(str(self.get_value(node_path)), False, (0, 0, 0))

        position = self.get_position(node_path)
        position = (position[0] - value_text.get_width() / 2, position[1] - value_text.get_height() / 2)
        screen.blit(value_text, position)

    def render_connection(self, screen, node_path):
        """Renders a line between two nodes. The line will be drawn from node at the given node path
        to its parent.

        Args:
            screen (pygame.Surface): The screen the connection will be rendered on.
            node_path (list): The path to the node. A list of column indices of all of this node's parents.
        """
        draw.line(screen, (0, 0, 0), self.get_parent_position(node_path), self.get_position(node_path))

    def set_value(self, index, value):
        """Sets a value to the node at the given child index of the current parent.

        Args:
            index (int): The child index of the current parent.
            value (int): The value to give to the node.
        """
        copy_parent = self.__parent.copy()
        copy_parent.append(index)
        path = tuple(copy_parent)
        self.__nodes[path] = (value, self.calculate_position(path))

    def get_parent_position(self, node_path):
        """Gets the position on the screen of the parent of the node at the given path.

        Args:
            node_path (list): The path to the node. A list of column indices of all of this node's parents.

        Returns:
            tuple: The position on the screen.
        """
        return self.get_position(node_path[:-1])

    def get_position(self, node_path):
        """Gets the position on the screen of the node at the given path.

        Args:
            node_path (list): The path to the node. A list of column indices of all of this node's parents.

        Returns:
            tuple: The position on the screen.
        """
        if len(node_path) == 0:
            return (self.__game.screen_width / 2, 150)

        return self.__nodes[node_path][1]

    def get_value(self, node_path):
        return self.__nodes[node_path][0]

    def calculate_position(self, node_path):
        """Calculates the position on the tree of the node at the given path.

        Args:
            node_path (list): The path to the node. A list of column indices of all of this node's parents.

        Returns:
            tuple: The position on the screen.
        """
        if len(node_path) == 0:
            return (self.__game.screen_width / 2, 150)

        y = (len(node_path) + 1) * 150
        x = self.calculate_parent_position(node_path)[0] + (node_path[-1] - 3) * 1100 / 8**len(node_path)

        return (x, y)

    def calculate_parent_position(self, node_path):
        """Calculates the position on the tree of the parent of the node at the given path.

        Args:
            node_path (list): The path to the node. A list of column indices of all of this node's parents.

        Returns:
            tuple: The position on the screen.
        """
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
        """Deletes all nodes from the tree.
        """
        self.__nodes = {}
        self.__nodes[()] = (None, self.get_position(()))

    def flip_use_visualizer(self):
        self.__use_visualizer = not self.__use_visualizer