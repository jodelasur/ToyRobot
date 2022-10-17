import fileinput

from toy_robot.core import App, CommandIgnored


def main():
    app = App()
    for line in fileinput.input():
        try:
            if result := app.process_command(line.strip()):
                print(result)
        except CommandIgnored:
            # Silently ignore commands
            pass


if __name__ == "__main__":
    main()
