from itertools import cycle

cart_symbols = "^<v>"


class Cart:

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y

        if direction not in cart_symbols:
            raise ValueError(str(direction) + " not a valid cart direction!")
        self.dir = direction
        self.next_turn = "left"

        # A repeating iterator of cart symbols to simplify turning cart
        self.dir_cycle = self.init_cycle()
        self.start = (x, y)

    def init_cycle(self):
        dir_cycle = cycle(cart_symbols)

        while True:
            current = next(dir_cycle)
            if current == self.dir:
                return dir_cycle

    def move(self):
        if self.dir == "^":
            self.y += -1
        elif self.dir == "v":
            self.y += 1
        elif self.dir == "<":
            self.x += -1
        elif self.dir == ">":
            self.x += 1

    def turn(self):
        """
        Cart goes left the first time, straight the second time,
        right the third time, and then repeats those directions
        """
        if self.next_turn == "left":
            self.left()
            self.next_turn = None
        elif self.next_turn == "right":
            self.right()
            self.next_turn = "left"
        else:
            self.next_turn = "right"

    def left(self):
        self.dir = next(self.dir_cycle)

    def right(self):
        # Three steps in the dir cycle results in a right turn
        next(self.dir_cycle)
        next(self.dir_cycle)
        self.dir = next(self.dir_cycle)

    def __repr__(self):
        return str(self.dir) + " (" + str(self.x) + "," + str(self.y) + ")"

    def __lt__(self, other):
        if self.y == other.y:
            return self.x < other.x

        return self.y < other.y

    def verbose_repr(self):
        return self.__repr__() + "\n  start: " + str(self.start)
