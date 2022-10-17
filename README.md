# Toy Robot - Jodel Asur

![Build and test](https://github.com/jodelasur/ToyRobot/actions/workflows/build_and_test.yaml/badge.svg)

My implementation of the coding challenge based on a blog post by Jon Eaves. Read it
here: https://joneaves.wordpress.com/2014/07/21/toy-robot-coding-test/

## Run the console app

```shell
virtualenv venv
source venv/bin/activate
python cli.py
```

## Commands

### PLACE X,Y,F

Put the toy robot on the table in position X,Y and facing NORTH, SOUTH, EAST or WEST.

### MOVE

Move the toy robot one unit forward in the direction it is currently facing.

### LEFT

Rotate the robot 90 degrees left without changing the position of the robot.

### RIGHT

Rotate the robot 90 degrees right without changing the position of the robot.

### REPORT

Print the robot's position.

## Examples

```
a)----------------
PLACE 0,0,NORTH
MOVE
REPORT
Output: 0,1,NORTH

b)----------------
PLACE 0,0,NORTH
LEFT
REPORT
Output: 0,0,WEST

c)----------------
PLACE 1,2,EAST
MOVE
MOVE
LEFT
MOVE
REPORT
Output: 3,3,NORTH
```

## Run tests

```shell
pip install -r requirements.test.txt
python -m pytest
```

## For auto-formatting and linting on commit

```shell
pip install -r requirements.dev.txt
pre-commit install
```
