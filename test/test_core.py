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

    placed_robot.process_command("REPORT")

    mock_report.assert_called_once()
    captured = capsys.readouterr()
    # Check if report is printed
    assert captured.out == f"{expected_report_return}\n"


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
    assert robot.x == 0
    assert robot.y == 0
    assert robot.f == "NORTH"


def test_place_again_after_placed(placed_robot):
    placed_robot.place(2, 2, "NORTH")
    assert (placed_robot.x, placed_robot.y, placed_robot.f) == (2, 2, "NORTH")


@pytest.mark.parametrize('f,place_after_move', [
    ("NORTH", (1, 2, "NORTH")),
    ("EAST", (2, 1, "EAST")),
    ("SOUTH", (1, 0, "SOUTH")),
    ("WEST", (0, 1, "WEST")),
])
def test_move(f, place_after_move):
    robot = Robot()
    robot.place(1, 1, f)
    robot.move()
    assert (robot.x, robot.y, robot.f) == place_after_move


@pytest.mark.parametrize('destruction_place_args', [
    *[(i, 0, "SOUTH") for i in range(DIMENSIONS)],
    *[(DIMENSIONS, i, "EAST") for i in range(DIMENSIONS)],
    *[(i, DIMENSIONS, "NORTH") for i in range(DIMENSIONS)],
    *[(0, i, "WEST") for i in range(DIMENSIONS)],
])
def test_move_prevent_destruction(destruction_place_args):
    robot = Robot()
    robot.place(*destruction_place_args)
    robot.move()

    # Robot doesn't move; fall to destruction prevented
    assert (robot.x, robot.y, robot.f) == destruction_place_args


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
    assert robot.x == 0
    assert robot.y == 0
    assert robot.f == new_f


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
    assert robot.x == 0
    assert robot.y == 0
    assert robot.f == new_f


def test_ignore_until_first_place():
    robot = Robot()

    # Ignore following commands since place command hasn't been done yet
    robot.move()
    robot.left()
    robot.right()
    robot.report()

    assert (robot.x, robot.y, robot.f) == (None, None, None)