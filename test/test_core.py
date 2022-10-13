import pytest
from pytest_mock import MockFixture

from toy_robot.core import Robot, DIMENSIONS


@pytest.fixture
def placed_robot():
    robot = Robot()
    robot.place(0, 0, "NORTH")
    return robot


def test_process_command_place(mocker: MockFixture):
    mock_place = mocker.patch('toy_robot.core.Robot.place')
    robot = Robot()
    robot.process_command("PLACE 0,0,NORTH")
    mock_place.assert_called_once_with(0, 0, 'NORTH')


def test_process_command_move(mocker: MockFixture, placed_robot):
    mock_move = mocker.patch('toy_robot.core.Robot.move')
    placed_robot.process_command("MOVE")
    mock_move.assert_called_once()


def test_process_command_report(mocker: MockFixture, placed_robot, capsys):
    mock_report = mocker.patch('toy_robot.core.Robot.report')
    expected_report_return = "0,0,NORTH"
    mock_report.return_value = expected_report_return

    ret = placed_robot.process_command("REPORT")

    mock_report.assert_called_once()
    assert ret == expected_report_return


def test_process_command_left(mocker: MockFixture, placed_robot):
    mock_left = mocker.patch('toy_robot.core.Robot.left')
    placed_robot.process_command("LEFT")
    mock_left.assert_called_once()


def test_process_command_right(mocker: MockFixture, placed_robot):
    mock_right = mocker.patch('toy_robot.core.Robot.right')
    placed_robot.process_command("RIGHT")
    mock_right.assert_called_once()


def test_place():
    robot = Robot()
    robot.place(0, 0, "NORTH")
    assert robot._x == 0
    assert robot._y == 0
    assert robot._f == "NORTH"


def test_place_again_after_placed(placed_robot):
    placed_robot.place(2, 2, "NORTH")
    assert (placed_robot._x, placed_robot._y, placed_robot._f) == (2, 2, "NORTH")


@pytest.mark.parametrize('x', [-1, DIMENSIONS])
def test_place_ignore_if_x_out_of_bounds(x):
    robot = Robot()
    robot.place(x, 0, "NORTH")
    assert (robot._x, robot._y, robot._f) == (None, None, None)


@pytest.mark.parametrize('y', [-1, DIMENSIONS])
def test_place_ignore_if_y_out_of_bounds(y):
    robot = Robot()
    robot.place(0, y, "NORTH")
    assert (robot._x, robot._y, robot._f) == (None, None, None)


def test_place_invalid_f_ignored():
    robot = Robot()
    robot.place(0, 0, "SOMEWHERE")
    assert (robot._x, robot._y, robot._f) == (None, None, None)


@pytest.mark.parametrize('f,new_x,new_y', [
    ("NORTH", 1, 4),
    ("EAST", 2, 3),
    ("SOUTH", 1, 2),
    ("WEST", 0, 3),
])
def test_move(f, new_x, new_y):
    robot = Robot()
    robot.place(1, 3, f)
    robot.move()
    assert (robot._x, robot._y, robot._f) == (new_x, new_y, f)


@pytest.mark.parametrize('x,y,f', [
    *[(i, 0, "SOUTH") for i in range(DIMENSIONS)],
    *[(DIMENSIONS - 1, i, "EAST") for i in range(DIMENSIONS)],
    *[(i, DIMENSIONS - 1, "NORTH") for i in range(DIMENSIONS)],
    *[(0, i, "WEST") for i in range(DIMENSIONS)],
])
def test_move_prevent_destruction(x, y, f):
    robot = Robot()
    robot.place(x, y, f)
    robot.move()

    # Robot doesn't move; fall to destruction prevented
    assert (robot._x, robot._y, robot._f) == (x, y, f)


def test_report(placed_robot):
    result = placed_robot.report()
    assert result == "0,0,NORTH"


@pytest.mark.parametrize("f,new_f", [
    ("NORTH", "WEST"),
    ("EAST", "NORTH"),
    ("SOUTH", "EAST"),
    ("WEST", "SOUTH"),
])
def test_left(f, new_f):
    robot = Robot()
    robot.place(0, 0, f)
    robot.left()
    assert robot._x == 0
    assert robot._y == 0
    assert robot._f == new_f


@pytest.mark.parametrize("f,new_f", [
    ("NORTH", "EAST"),
    ("EAST", "SOUTH"),
    ("SOUTH", "WEST"),
    ("WEST", "NORTH"),
])
def test_right(f, new_f):
    robot = Robot()
    robot.place(0, 0, f)
    robot.right()
    assert robot._x == 0
    assert robot._y == 0
    assert robot._f == new_f


def test_ignore_until_first_place():
    robot = Robot()

    # Ignore following commands since place command hasn't been done yet
    robot.move()
    robot.left()
    robot.right()
    robot.report()

    assert (robot._x, robot._y, robot._f) == (None, None, None)


def test_bug_1():
    robot = Robot()
    robot.place(4, 2, "EAST")
    robot.right()
    robot.move()
    assert robot.report() == f"4,1,SOUTH"
