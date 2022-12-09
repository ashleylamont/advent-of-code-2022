class RopePair:
    def __init__(self):
        self.chained = None
        self.head = [0, 0]
        self.tail = [0, 0]

    def add_chained(self, other):
        self.chained = other

    def move_head(self, movement_x: int, movement_y: int):
        self.head[0] += movement_x
        self.head[1] += movement_y

        self.move_tail()

    def move_tail(self):
        horizontal_difference = self.head[0] - self.tail[0]
        vertical_difference = self.head[1] - self.tail[1]

        if abs(horizontal_difference) <= 1 and abs(vertical_difference) <= 1:
            return

        x_delta = 0
        y_delta = 0
        if horizontal_difference != 0:
            x_delta = horizontal_difference / abs(horizontal_difference)
        if vertical_difference != 0:
            y_delta = vertical_difference / abs(vertical_difference)
        self.tail[0] += x_delta
        self.tail[1] += y_delta

        if self.chained is not None:
            self.chained.move_head(x_delta, y_delta)
