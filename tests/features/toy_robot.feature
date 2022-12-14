Feature: Toy Robot App

  # Rule: Any movement that would result in the robot falling from the table must be prevented,
  #       however further valid movement commands must still be allowed.

  Scenario Outline: Prevent robot from falling
    Given a robot placed at <x>,<y>,<f>
    When a user gives the MOVE command
    Then the command is ignored
    And the robot does not move from <x>,<y>
    And the robot faces <f>

    Examples:
      | x | y | f     |
      | 2 | 4 | NORTH |
      | 2 | 0 | SOUTH |
      | 4 | 2 | EAST  |
      | 0 | 2 | WEST  |

  # Rule: PLACE will put the toy robot on the table in position X,Y and facing NORTH, SOUTH, EAST or WEST.

  Scenario: Valid PLACE command
    Given a 5x5 table with no robots
    When a user gives the command "PLACE 0,0,NORTH"
    Then the robot is placed in 0,0,NORTH

  Scenario Outline: Invalid PLACE command
    Given a 5x5 table with no robots
    When a user gives the command "PLACE <invalid_pos>"
    Then the command is ignored

    Examples:
      | invalid_pos |
      | -1,0,NORTH  |
      | 5,0,NORTH   |
      | 0,-1,NORTH  |
      | 0,5,NORTH   |
      | 0,0,INVALID |

  Scenario Outline: Valid f values
    Given a 5x5 table with no robots
    When a user gives the command PLACE 0,0,<f>
    Then the robot is placed in 0,0,<f>

    Examples:
      | f     |
      | NORTH |
      | SOUTH |
      | EAST  |
      | WEST  |

  # Rule: It is required that the first command to the robot is a PLACE command,
  #       after that, any sequence of commands may be issued, in any order, including another PLACE command.
  #       The application should discard all commands in the sequence until a valid PLACE command has been executed.

  Scenario Outline: Invalid first command
    Given a 5x5 table with no robots
    When a user gives the command <cmd>
    Then the command is ignored

    Examples:
      | cmd    |
      | MOVE   |
      | LEFT   |
      | RIGHT  |
      | REPORT |

  Scenario Outline: Valid command after first PLACE
    Given a 5x5 table with no robots
    And a user gives the command "PLACE 0,0,NORTH"
    When a user gives the command <cmd>
    Then the command is processed

    Examples:
      | cmd             |
      | MOVE            |
      | LEFT            |
      | RIGHT           |
      | REPORT          |
      | PLACE 2,2,NORTH |

  # Rule: MOVE will move the toy robot one unit forward in the direction it is currently facing.

  Scenario Outline: MOVE command
    Given a robot placed at 1,3,<f>
    When a user gives the MOVE command
    Then the robot moves one unit forward in the direction it is currently facing, at <new_x>,<new_y>,<f>

    Examples:
      | f     | new_x | new_y |
      | NORTH | 1     | 4     |
      | EAST  | 2     | 3     |
      | SOUTH | 1     | 2     |
      | WEST  | 0     | 3     |

  # Rule: LEFT and RIGHT will rotate the robot 90 degrees in the specified direction without
  # changing the position of the robot.

  Scenario Outline: LEFT command
    Given a robot placed at <x>,<y>,<f>
    When a user gives the LEFT command
    Then the robot faces <new_f>
    And the robot does not move from <x>,<y>

    Examples:
      | x | y | f     | new_f |
      | 2 | 2 | NORTH | WEST  |
      | 2 | 2 | EAST  | NORTH |
      | 2 | 2 | SOUTH | EAST  |
      | 2 | 2 | WEST  | SOUTH |

  Scenario Outline: RIGHT command
    Given a robot placed at <x>,<y>,<f>
    When a user gives the RIGHT command
    Then the robot faces <new_f>
    And the robot does not move from <x>,<y>

    Examples:
      | x | y | f     | new_f |
      | 2 | 2 | NORTH | EAST  |
      | 2 | 2 | EAST  | SOUTH |
      | 2 | 2 | SOUTH | WEST  |
      | 2 | 2 | WEST  | NORTH |

  # Rule: REPORT will announce the X,Y and F of the robot.

  Scenario Outline: REPORT command
    Given a robot placed at <x>,<y>,<f>
    When a user gives the REPORT command
    Then the app reports <position_csv>

    Examples:
      | x | y | f     | position_csv |
      | 0 | 0 | NORTH | 0,0,NORTH    |

  # Rule: A robot that is not on the table can choose to ignore the MOVE, LEFT, RIGHT and REPORT commands.

  Scenario Outline: Robot ignores command if not on table
    Given a robot not on the table
    When a <command> is given to the robot
    Then the robot ignores the command

    Examples:
      | command         |
      | MOVE            |
      | LEFT            |
      | RIGHT           |
      | REPORT          |