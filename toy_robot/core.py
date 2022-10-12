import re


class Robot:
    def __init__(self):
        self.x = None
        self.y = None
        self.f = None

    def process_command(self, cmd):
        if m := re.match(r"PLACE (\d),(\d),(\w+)", cmd):
            x_str, y_str, f = m.groups()
            self._place(int(x_str), int(y_str), f)
        elif cmd == "MOVE":
            self._move()

    def _place(self, x: int, y: int, f: str):
        self.x = x
        self.y = y
        self.f = f

    def _move(self):
        if self.f == "NORTH":
            self.y = self.y + 1
        elif self.f == "SOUTH":
            self.y = self.y - 1
        elif self.f == "EAST":
            self.x = self.x + 1
        elif self.f == "WEST":
            self.x = self.x - 1