import re

# Directions, ordered clockwise
DIRECTIONS = ["NORTH", "EAST", "SOUTH", "WEST"]
LEFT = {DIRECTIONS[i]: DIRECTIONS[(i - 1) % len(DIRECTIONS)] for i in range(len(DIRECTIONS))}


class Robot:
    def __init__(self):
        self.x = None
        self.y = None
        self.f = None

    def process_command(self, cmd):
        if m := re.match(r"PLACE (\d),(\d),(\w+)", cmd):
            x_str, y_str, f = m.groups()
            self.place(int(x_str), int(y_str), f)
        elif cmd == "MOVE":
            self.move()
        elif cmd == "LEFT":
            self.left()

    def place(self, x: int, y: int, f: str):
        self.x = x
        self.y = y
        self.f = f

    def move(self):
        if self.f == "NORTH":
            self.y = self.y + 1
        elif self.f == "SOUTH":
            self.y = self.y - 1
        elif self.f == "EAST":
            self.x = self.x + 1
        elif self.f == "WEST":
            self.x = self.x - 1

    def left(self):
        self.f = LEFT[self.f]
