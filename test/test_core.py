import pytest
from pytest_mock import MockFixture

from toy_robot.core import Robot

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


def test_process_command_left(mocker: MockFixture, placed_robot):
    mock_left = mocker.patch('toy_robot.core.Robot.left')
    placed_robot.process_command("LEFT")
    mock_left.assert_called_once()


def test_place():
    robot = Robot()
    robot.place(0, 0, "NORTH")
    assert robot.x == 0
    assert robot.y == 0
    assert robot.f == "NORTH"


def test_move(placed_robot):
    placed_robot.move()
    assert placed_robot.x == 0
    assert placed_robot.y == 1
    assert placed_robot.f == "NORTH"


def test_left():
    robot = Robot()
    robot.process_command("PLACE 0,0,NORTH")
    robot.process_command("LEFT")
    assert robot.x == 0
    assert robot.y == 0
    assert robot.f == "WEST"
