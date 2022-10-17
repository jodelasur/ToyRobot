Feature: Toy Robot App

  Rule: PLACE will put the toy robot on the table in position X,Y and facing NORTH, SOUTH, EAST or WEST.

    Scenario: Valid PLACE command
      Given a 5x5 table with no robots
      When a user gives the command "PLACE 0,0,NORTH"
      Then the robot is placed in 0,0,NORTH

    Scenario Outline: Invalid PLACE command
      Given a 5x5 table with no robots
      When a user gives the command "PLACE <invalid_pos>"
      Then no robot is placed on the table

      Examples:
        | invalid_pos |
        | -1,0,NORTH  |
        | 5,0,NORTH   |
        | 0,-1,NORTH  |
        | 0,5,NORTH   |
        | 0,0,INVALID |

