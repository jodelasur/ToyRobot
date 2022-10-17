import pytest

from toy_robot.core import App, CommandIgnored, Robot, Table


class TestApp:
    def test_move(self):
        app = App()
        app.process_command("PLACE 1,3,NORTH")
        app.process_command("MOVE")

        assert app.table.robot.position == (1, 4, "NORTH")

    def test_prevent_robot_from_falling(self):
        app = App()
        app.process_command("PLACE 2,4,NORTH")

        with pytest.raises(CommandIgnored):
            app.process_command("MOVE")

    def test_report(self):
        app = App()
        app.process_command("PLACE 1,3,NORTH")

        result = app.process_command("REPORT")

        assert result == "1,3,NORTH"


class TestTable:
    def test_place_robot(self):
        table = Table()
        table.place_robot(0, 0, "NORTH")
        assert table.robot.position == (0, 0, "NORTH")

    def test_move_robot(self):
        table = Table()
        table.place_robot(1, 3, "NORTH")

        table.move_robot()

        assert table.robot.position == (1, 4, "NORTH")

    def test_prevent_robot_from_falling(self):
        table = Table()
        table.place_robot(2, 4, "NORTH")

        with pytest.raises(CommandIgnored):
            table.move_robot()

    def test_report_robot(self):
        table = Table()
        table.place_robot(1, 3, "NORTH")

        result = table.report_robot()

        assert result == "1,3,NORTH"


class TestRobot:
    def test_is_placed(self):
        robot = Robot()
        assert robot.is_placed is False

    def test_placed_robot_is_placed(self):
        robot = Robot()
        robot.place(0, 0, "NORTH")
        assert robot.is_placed is True

    def test_move_ignore_until_placed(self):
        robot = Robot()
        with pytest.raises(CommandIgnored):
            robot.move()

    def test_move_not_ignored_if_placed(self):
        robot = Robot()
        robot.place(0, 0, "NORTH")
        # No exception should be raised
        robot.move()

    def test_move(self):
        robot = Robot()
        robot.place(1, 3, "NORTH")
        robot.move()
        assert robot.position == (1, 4, "NORTH")

    def test_report(self):
        robot = Robot()
        robot.place(1, 3, "NORTH")

        result = robot.report()

        assert result == "1,3,NORTH"


def test_fail_github_actions():
    raise NotImplementedError("I failed. :/")
