import re

# Directions, ordered clockwise
DIRECTIONS = ["NORTH", "EAST", "SOUTH", "WEST"]
LEFT = {DIRECTIONS[i]: DIRECTIONS[(i - 1) % len(DIRECTIONS)] for i in range(len(DIRECTIONS))}
RIGHT = {DIRECTIONS[i]: DIRECTIONS[(i + 1) % len(DIRECTIONS)] for i in range(len(DIRECTIONS))}

DIMENSIONS = 5


def ignore_until_placed(function):
    def wrapper(*args, **kwargs):
        self = args[0]
        # If robot is not yet placed, ignore
        if any([item is None for item in (self.x, self.y, self.f)]):
            return
        return function(*args, **kwargs)

    return wrapper


class Robot:
    def __init__(self):
        self.x = None
        self.y = None
        self.f = None

    def process_command(self, cmd):
        if m := re.match(r"PLACE (\d),(\d),(\w+)", cmd):
            x_str, y_str, f = m.groups()
            self.place(int(x_str), int(y_str), f)

        if any([item is None for item in (self.x, self.y, self.f)]):
            return

        if cmd == "MOVE":
            self.move()
        elif cmd == "REPORT":
            print(self.report())
        elif cmd == "LEFT":
            self.left()
        elif cmd == "RIGHT":
            self.right()

    def place(self, x: int, y: int, f: str):
        self.x = x
        self.y = y
        self.f = f

    @ignore_until_placed
    def move(self):
        new_pos = self.x, self.y

        if self.f == "NORTH":
            new_pos = self.x, self.y + 1
        elif self.f == "SOUTH":
            new_pos = self.y, self.y - 1
        elif self.f == "EAST":
            new_pos = self.x + 1, self.y
        elif self.f == "WEST":
            new_pos = self.x - 1, self.y

        # If new_pos is not out of bounds
        if not any([coord < 0 or coord >= DIMENSIONS for coord in new_pos]):
            self.x, self.y = new_pos

    @ignore_until_placed
    def report(self):
        return f"{self.x},{self.y},{self.f}"

    @ignore_until_placed
    def left(self):
        self.f = LEFT[self.f]

    @ignore_until_placed
    def right(self):
        self.f = RIGHT[self.f]
