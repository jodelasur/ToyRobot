from pytest_bdd import given, parsers, scenarios, then, when

from toy_robot.core_v2 import App, CommandIgnored

scenarios("../features/toy_robot.feature")


@given("a 5x5 table with no robots", target_fixture="app")
def app():
    return App()


@given('a user gives the command "PLACE 0,0,NORTH"')
@when('a user gives the command "PLACE 0,0,NORTH"')
def step_impl(app):
    app.process_command("PLACE 0,0,NORTH")


@then("the robot is placed in 0,0,NORTH")
def step_impl(app):
    assert app.table.robot.position == (0, 0, "NORTH")


@then("no robot is placed on the table")
def step_impl(app):
    assert app.table.robot is None


@when(
    parsers.parse('a user gives the command "PLACE {invalid_pos}"'),
    target_fixture="raised_exception",
)
def step_impl(app, invalid_pos):
    try:
        app.process_command(f"PLACE {invalid_pos}")
    except CommandIgnored as e:
        return e


@when(parsers.parse("a user gives the command PLACE 0,0,{f}"))
def step_impl(app, f):
    app.process_command(f"PLACE 0,0,{f}")


@then(parsers.parse("the robot is placed in 0,0,{f}"))
def step_impl(app, f):
    assert app.table.robot.position == (0, 0, f)


@when(
    parsers.parse("a user gives the command {cmd}"),
    target_fixture="raised_exception",
)
def step_impl(app, cmd):
    try:
        app.process_command(cmd)
    except CommandIgnored as e:
        return e


@then("the command is ignored")
def step_impl(app, raised_exception):
    assert isinstance(raised_exception, CommandIgnored)


@then("the command is processed")
def step_impl(raised_exception):
    assert raised_exception is None


@given(parsers.parse("a robot placed at 1,3,{f}"), target_fixture="app_robot_at_1_3")
@given("a robot placed at 1,3,<f>")
def app_robot_at_1_3(f):
    app = App()
    app.process_command(f"PLACE 1,3,{f}")

    return app


@when("a user gives the MOVE command")
def step_impl(app_robot_at_1_3):
    app_robot_at_1_3.process_command("MOVE")


@then(
    parsers.parse(
        "the robot moves one unit forward in the direction it is currently facing, "
        "at {new_x:d},{new_y:d},{f}"
    )
)
@then(
    "the robot moves one unit forward in the direction it is currently facing, "
    "at <new_x>,<new_y>,<f>"
)
def step_impl(app_robot_at_1_3, new_x, new_y, f):
    assert app_robot_at_1_3.table.robot.position == (new_x, new_y, f)
