import re


class Robot:
    def __init__(self, x: int, y: int, f: str):
        self.x = x
        self.y = y
        self.f = f


class Table:
    robot = None

    def process_command(self, cmd):
        if m := re.match(r"PLACE (\d),(\d),(\w+)", cmd):
            x_str, y_str, f = m.groups()
            self.robot = Robot(int(x_str), int(y_str), f)
