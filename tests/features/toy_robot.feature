Feature: Toy Robot App

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
