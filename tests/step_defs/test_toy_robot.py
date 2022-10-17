from pytest_bdd import given, parsers, scenarios, then, when

from toy_robot.core_v2 import App

scenarios("../features/toy_robot.feature")


@given("a 5x5 table with no robots", target_fixture="app")
def app():
    return App()


@when('a user gives the command "PLACE 0,0,NORTH"')
def step_impl(app):
    app.process_command("PLACE 0,0,NORTH")


@then("the robot is placed in 0,0,NORTH")
def step_impl(app):
    assert app.table.robot.position == (0, 0, "NORTH")


@then("no robot is placed on the table")
def step_impl(app):
    assert app.table.robot is None


@when(parsers.parse('a user gives the command "PLACE {invalid_pos}"'))
def step_impl(app, invalid_pos):
    app.process_command(f"PLACE {invalid_pos}")
