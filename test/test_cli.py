import fileinput

from toy_robot.cli import main


def test_example_a(monkeypatch, capsys):
    monkeypatch.setattr(fileinput, 'input', open("test/fixtures/example_a_input.txt").readlines)
    main()
    captured = capsys.readouterr()
    assert captured.out == "0,0,WEST\n"



