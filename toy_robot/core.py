import re

# Directions, ordered clockwise
DIRECTIONS = ["NORTH", "EAST", "SOUTH", "WEST"]
LEFT = {
    DIRECTIONS[i]: DIRECTIONS[(i - 1) % len(DIRECTIONS)] for i in range(len(DIRECTIONS))
}
RIGHT = {
    DIRECTIONS[i]: DIRECTIONS[(i + 1) % len(DIRECTIONS)] for i in range(len(DIRECTIONS))
}

DIMENSIONS = 5


def ignore_until_placed(function):
    def wrapper(*args, **kwargs):
        self = args[0]
        # If robot is not yet placed, ignore
        if any([item is None for item in (self._x, self._y, self._f)]):
            return
        return function(*args, **kwargs)

    return wrapper


class Robot:
    def __init__(self):
        self._x = None
        self._y = None
        self._f = None

    def process_command(self, cmd):
        if m := re.match(r"PLACE (\d),(\d),(\w+)", cmd):
            x_str, y_str, f = m.groups()
            self.place(int(x_str), int(y_str), f)

        if any([item is None for item in (self._x, self._y, self._f)]):
            return

        if cmd == "MOVE":
            self.move()
        elif cmd == "REPORT":
            return self.report()
        elif cmd == "LEFT":
            self.left()
        elif cmd == "RIGHT":
            self.right()

    def place(self, x: int, y: int, f: str):
        if self.is_out_of_bounds(x) or self.is_out_of_bounds(y) or f not in DIRECTIONS:
            return

        self._x = x
        self._y = y
        self._f = f

    @ignore_until_placed
    def move(self):
        new_pos = self._x, self._y

        if self._f == "NORTH":
            new_pos = self._x, self._y + 1
        elif self._f == "SOUTH":
            new_pos = self._x, self._y - 1
        elif self._f == "EAST":
            new_pos = self._x + 1, self._y
        elif self._f == "WEST":
            new_pos = self._x - 1, self._y

        # If new_pos is not out of bounds
        if not any([coord < 0 or coord >= DIMENSIONS for coord in new_pos]):
            self._x, self._y = new_pos

    @ignore_until_placed
    def report(self):
        return f"{self._x},{self._y},{self._f}"

    @ignore_until_placed
    def left(self):
        self._f = LEFT[self._f]

    @ignore_until_placed
    def right(self):
        self._f = RIGHT[self._f]

    @staticmethod
    def is_out_of_bounds(coord: int):
        return coord < 0 or coord >= DIMENSIONS
