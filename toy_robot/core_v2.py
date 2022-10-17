from __future__ import annotations

import re

# Directions, ordered clockwise
DIRECTIONS = ["NORTH", "EAST", "SOUTH", "WEST"]
LEFT = {
    DIRECTIONS[i]: DIRECTIONS[(i - 1) % len(DIRECTIONS)] for i in range(len(DIRECTIONS))
}
RIGHT = {
    DIRECTIONS[i]: DIRECTIONS[(i + 1) % len(DIRECTIONS)] for i in range(len(DIRECTIONS))
}


class App:
    def __init__(self):
        self._table = Table()

    def process_command(self, cmd):
        if m := re.match(r"PLACE (\d),(\d),(\w+)", cmd):
            x_str, y_str, f = m.groups()
            self._table.place_robot(int(x_str), int(y_str), f)
        elif cmd == "MOVE":
            self._table.move_robot()
        elif cmd == "LEFT":
            self._table.left_robot()
        elif cmd == "RIGHT":
            self._table.right_robot()
        elif cmd == "REPORT":
            self._table.report_robot()
        else:
            raise CommandIgnored("Invalid command")

    @property
    def table(self):
        return self._table


class Table:
    def __init__(self):
        self._dimensions: int = 5
        self._robot: Robot = Robot()

    @property
    def robot(self):
        return self._robot

    def place_robot(self, x: int, y: int, f: str):
        if self.is_out_of_bounds(x, y) or f not in DIRECTIONS:
            raise CommandIgnored("Invalid place arguments")

        self._robot.place(x, y, f)

    def is_out_of_bounds(self, x: int, y: int):
        return any([coord < 0 or coord >= self._dimensions for coord in (x, y)])

    def move_robot(self):
        self._robot.move()

    def left_robot(self):
        self._robot.left()

    def right_robot(self):
        self._robot.right()

    def report_robot(self):
        self._robot.report()


def ignore_until_placed(function):
    def wrapper(*args, **kwargs):
        self = args[0]
        if not self.is_placed:
            raise CommandIgnored("Robot not yet placed")
        return function(*args, **kwargs)

    return wrapper


class Robot:
    def __init__(self):
        self._x = None
        self._y = None
        self._f = None

    def place(self, x: int, y: int, f: str):
        self._x = x
        self._y = y
        self._f = f

    @property
    def position(self):
        return self._x, self._y, self._f

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

        self._x, self._y = new_pos

    @ignore_until_placed
    def left(self):
        self._f = LEFT[self._f]

    @ignore_until_placed
    def right(self):
        self._f = RIGHT[self._f]

    @ignore_until_placed
    def report(self):
        pass

    @property
    def is_placed(self):
        return all([item is not None for item in (self._x, self._y, self._f)])


class CommandIgnored(Exception):
    pass
