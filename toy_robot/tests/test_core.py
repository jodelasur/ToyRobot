from toy_robot.core import Robot


def test_place():
    robot = Robot()
    robot.process_command("PLACE 0,0,NORTH")
    assert robot.x == 0
    assert robot.y == 0
    assert robot.f == "NORTH"
