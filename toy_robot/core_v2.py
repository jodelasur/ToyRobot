import re


class App:
    def __init__(self):
        self._table = Table()

    def process_command(self, cmd):
        if m := re.match(r"PLACE (\d),(\d),(\w+)", cmd):
            x_str, y_str, f = m.groups()
            self._table.place_robot(int(x_str), int(y_str), f)

    @property
    def table(self):
        return self._table


class Table:
    def __init__(self):
        self._dimensions = 5
        self._robot = None

    @property
    def robot(self):
        return self._robot

    def place_robot(self, x: int, y: int, f: str):
        self._robot = Robot(x, y, f)


class Robot:
    def __init__(self, x: int, y: int, f: str):
        self._x = x
        self._y = y
        self._f = f

    @property
    def position(self):
        return self._x, self._y, self._f
