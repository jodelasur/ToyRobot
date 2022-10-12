from toy_robot.core import Table


def test_place_command():
    table = Table()
    table.process_command("PLACE 0,0,NORTH")
    assert table.robot.x == 0
    assert table.robot.y == 0
    assert table.robot.f == "NORTH"
