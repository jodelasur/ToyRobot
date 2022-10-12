import fileinput


def main():
    table = Table()
    for line in fileinput.input():
        table.process_command(line)


if __name__ == '__main__':
    main()
