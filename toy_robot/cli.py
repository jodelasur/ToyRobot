import fileinput

from toy_robot.core import Robot


def main():
    robot = Robot()
    for line in fileinput.input():
        robot.process_command(line)


if __name__ == '__main__':
    main()
