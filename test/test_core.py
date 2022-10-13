from toy_robot.core import Robot


def test_place():
    robot = Robot()
    robot.process_command("PLACE 0,0,NORTH")
    assert robot.x == 0
    assert robot.y == 0
    assert robot.f == "NORTH"


def test_move():
    robot = Robot()
    robot.process_command("PLACE 0,0,NORTH")
    robot.process_command("MOVE")
    assert robot.x == 0
    assert robot.y == 1
    assert robot.f == "NORTH"


def test_left():
    robot = Robot()
    robot.process_command("PLACE 0,0,NORTH")
    robot.process_command("LEFT")
    assert robot.x == 0
    assert robot.y == 0
    assert robot.f == "WEST"
