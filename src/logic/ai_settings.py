class AISettings:
    def __init__(self, iterative_deepening, alpha_beta, max_depth, order_moves) -> None:
        self.iterative_deepening = iterative_deepening
        self.alpha_beta = alpha_beta
        self.max_depth = max_depth
        self.order_moves = order_moves

    def flip_iterative_deepening(self):
        self.iterative_deepening = not self.iterative_deepening

    def flip_alpha_beta(self):
        self.alpha_beta = not self.alpha_beta

    def flip_order_moves(self):
        self.order_moves = not self.order_moves

    def set_max_depth(self, depth):
        if not isinstance(depth, int):
            try:
                depth = int(depth())
            except (TypeError, ValueError):
                return

        if depth < 1:
            return

        self.max_depth = depth

    def get_max_depth(self):
        return self.max_depth