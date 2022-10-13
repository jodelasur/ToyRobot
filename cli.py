import fileinput

from toy_robot.core import Robot


def main():
    robot = Robot()
    for line in fileinput.input():
        if result := robot.process_command(line.strip()):
            print(result)


if __name__ == '__main__':
    main()
