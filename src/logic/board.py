class Board:
    def __init__(self) -> None:
        self.__board_list = []
        for i in range(6):
            self.__board_list.append([0]*7)

    def get_slot(self, x, y):
        return self.__board_list[y][x]
    
    def set_slot(self, x, y, controller_number):
        self.__board_list[y][x] = controller_number

    def drop(self, x, controller_number):
        for i in range(-1, -len(self.__board_list) - 1, -1):
            if self.get_slot(x, i) == 0:
                self.set_slot(x, i, controller_number)
                return

        raise ValueError("Column is full")