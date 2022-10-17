import fileinput

import pytest

from cli import main


@pytest.mark.parametrize(
    "input_filepath,expected_out",
    [
        ("tests/example_inputs/a.txt", "0,1,NORTH\n"),
        ("tests/example_inputs/b.txt", "0,0,WEST\n"),
        ("tests/example_inputs/c.txt", "3,3,NORTH\n"),
    ],
)
def test_example_inputs(monkeypatch, capsys, input_filepath, expected_out):
    with open(input_filepath) as input_file:
        monkeypatch.setattr(fileinput, "input", input_file.readlines)
        main()

    captured = capsys.readouterr()
    assert captured.out == expected_out
